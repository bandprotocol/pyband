import json
import pytest
import random
import math
import hashlib
import string

from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_string_canonize
from bip32 import BIP32
from bech32 import bech32_encode, convertbits
from mnemonic import Mnemonic

from pyband.exceptions import *
from pyband.cosmos_app import CosmosApp, CommException
from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.oracle.v1.tx_pb2 import MsgCreateDataSource
from pyband.transaction import Transaction
from pyband.wallet import Ledger, PrivateKey


MOCK_MNEMONIC = "coach pond canoe lake solution empty vacuum term pave toe burst top violin purpose umbrella color disease thrive diamond found track need filter wait"


class MockDongle:
    def __init__(self, mnemonic):
        self.mnemonic = MOCK_MNEMONIC
        self._packet_cache = None

    def _clear_cache(self):
        self._packet_cache = None

    def exchange(self, apdu: bytes, timeout: int = 60):
        if len(apdu) <= 4:
            raise CommException(LEDGER_RETURN_CODES.get("0x6f00", "UNKNOWN"), sw=0x6F00)
        cla = apdu[0]
        ins = apdu[1]
        p1 = apdu[2]
        p2 = apdu[3]
        l = apdu[4]
        data = apdu[5:]

        if cla != 0x55:
            raise CommException(LEDGER_RETURN_CODES.get("0x6e00", "UNKNOWN"), sw=0x6E00)

        if ins == 0x00:
            return self._get_version()
        elif ins == 0x04:
            return self._ins_get_addr_secp256k1(p1, data)
        elif ins == 0x02:
            return self._sign_secp256k1(p1, data)
        else:
            raise CommException(LEDGER_RETURN_CODES.get("0x6d00", "UNKNOWN"), sw=0x6D00)

    def apduMaxDataSize(self):
        pass

    def close(self):
        pass

    def _get_version(self):
        return b"\x00\x02\x12\x00\x00\x33\x00\x00\x04"

    @staticmethod
    def __path_from_data(data: bytes, harden_count: int):
        # hrp_len = data[0]
        # bip32_byte = data[hrp_len + 1 :]
        path = "m/"
        for i in range(0, math.ceil(len(data) / 4)):
            if i < harden_count:
                idx = int.from_bytes(data[i * 4 : i * 4 + 3], "little")
                path += f"{idx}'/"
            else:
                idx = int.from_bytes(data[i * 4 : i * 4 + 4], "little")
                path += f"{idx}/"

        return path[:-1]

    def _ins_get_addr_secp256k1(self, p1: int, data: bytes):
        hrp_len = data[0]
        bip32_byte = data[hrp_len + 1 :]

        seed = Mnemonic("english").to_seed(self.mnemonic)
        signing_key = SigningKey.from_string(
            BIP32.from_seed(seed).get_privkey_from_path(self.__path_from_data(bip32_byte, 3)),
            curve=SECP256k1,
            hashfunc=hashlib.sha256,
        )

        verifying_key = signing_key.get_verifying_key()
        # five_bit_r = convertbits(bytes.fromhex("eb5ae98721") + verifying_key.to_string("compressed"), 8, 5)
        # bech32_addr = bytes(bech32_encode("band", five_bit_r), "utf-8")
        addr = hashlib.new("ripemd160", hashlib.new("sha256", verifying_key.to_string("compressed")).digest()).digest()
        five_bit_r = convertbits(addr, 8, 5)
        return verifying_key.to_string("compressed") + bytes(bech32_encode("band", five_bit_r), "utf-8")

    def _sign_secp256k1(self, p1: int, data: bytes):
        if p1 == 0:
            self.packet_cache = [data]
            return None
        elif p1 == 1:
            self.packet_cache.append(data)
            return None
        elif p1 == 2:
            self.packet_cache.append(data)

            signing_key = SigningKey.from_string(
                BIP32.from_seed(Mnemonic("english").to_seed(self.mnemonic)).get_privkey_from_path(
                    self.__path_from_data(self.packet_cache[0], 3)
                ),
                curve=SECP256k1,
                hashfunc=hashlib.sha256,
            )

            msg = b""
            for packet in self.packet_cache[1:]:
                msg += packet

            signed_msg = signing_key.sign_deterministic(
                msg,
                hashfunc=hashlib.sha256,
                sigencode=sigencode_string_canonize,
            )

            self._clear_cache()
            return signed_msg
            # return total_packets.to_bytes(1, "little")
        else:
            raise CommException(LEDGER_RETURN_CODES.get("0x6400", "UNKNOWN"), sw=0x6400)


class MockCosmosApp(CosmosApp):
    def __init__(self, derivation_path):
        self.dongle = MockDongle(derivation_path)
        self.derivation_path = derivation_path


@pytest.fixture()
def valid_derivation_path():
    return "m/44'/118'/0'/0/0"


@pytest.fixture()
def mock_cosmos_app(valid_derivation_path):
    return MockCosmosApp(valid_derivation_path)


@pytest.fixture()
def mock_ledger(mock_cosmos_app):
    return Ledger(
        derivation_path=mock_cosmos_app.derivation_path,
        cosmos_app=mock_cosmos_app,
    )


@pytest.fixture()
def mock_private_key(valid_derivation_path):
    return PrivateKey.from_mnemonic(MOCK_MNEMONIC, valid_derivation_path)


@pytest.fixture()
def mock_message():
    deploy_msg = MsgCreateDataSource(
        name="Hello World!",
        description="",
        executable=bytes("".join(random.choice(string.ascii_letters) for i in range(200)), "utf-8"),
        fee=[Coin(amount="0", denom="uband")],
        treasury="band000000000000000000000000000000000000000",
        owner="band000000000000000000000000000000000000000",
        sender="band000000000000000000000000000000000000000",
    )

    txn = (
        Transaction()
        .with_messages(deploy_msg)
        .with_sequence(0)
        .with_account_num(0)
        .with_chain_id("random_chain_id")
        .with_gas(50000)
        .with_fee([Coin(amount="50000", denom="uband")])
    )
    return txn


def test_get_version(mock_ledger):
    resp = mock_ledger.app_info()

    assert resp.cla == 0
    assert resp.major == 2
    assert resp.minor == 18
    assert resp.patch == 0


def test_ins_get_addr_secp257k1(mock_private_key, mock_ledger):
    comparison_public_key = mock_private_key.to_public_key()
    comparison_addr = comparison_public_key.to_address()

    resp = mock_ledger.get_pub_key_and_bech32_address()

    assert resp.public_key == comparison_public_key.verify_key.to_string("compressed")
    assert resp.address.decode("utf-8") == comparison_addr.to_acc_bech32()


def test_sign_secp256k1(mock_private_key, mock_ledger, mock_message):
    mock_public_key = mock_private_key.to_public_key()
    mock_sign_doc = mock_message.get_sign_doc(mock_public_key).SerializeToString()
    comparison_signed_msg = mock_private_key.sign(mock_sign_doc)

    resp = mock_ledger.sign(mock_sign_doc)

    assert comparison_signed_msg == resp
