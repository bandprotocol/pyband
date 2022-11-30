import hashlib
import random
import string

import math
import pytest
from bech32 import bech32_encode, convertbits
from bip32 import BIP32
from ecdsa.curves import SECP256k1
from ecdsa.der import encode_sequence, encode_integer, remove_sequence, remove_integer
from ecdsa.keys import SigningKey
from ecdsa.util import sigencode_string_canonize
from ledgerblue.Dongle import Dongle
from mnemonic import Mnemonic

from pyband import PrivateKey
from pyband.cosmos_app import CosmosApp, CommException
from pyband.exceptions import *
from pyband.messages.oracle.v1 import MsgCreateDataSource
from pyband.proto.cosmos.base.v1beta1 import Coin
from pyband.transaction import Transaction
from pyband.utils import bip44_to_list

MOCK_MNEMONIC = "coach pond canoe lake solution empty vacuum term pave toe burst top violin purpose umbrella color disease thrive diamond found track need filter wait"


class MockDongle(Dongle):
    def __init__(self):
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

            r = encode_integer(int.from_bytes(signed_msg[:32], "big"))
            s = encode_integer(int.from_bytes(signed_msg[32:], "big"))
            encoded = encode_sequence(r, s)

            return encoded
        else:
            raise CommException(LEDGER_RETURN_CODES.get("0x6400", "UNKNOWN"), sw=0x6400)


@pytest.fixture()
def valid_derivation_path():
    return "m/44'/118'/0'/0/0"


@pytest.fixture()
def mock_cosmos_app(valid_derivation_path):
    return CosmosApp(bip44_to_list(valid_derivation_path), dongle=MockDongle())


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
        .with_gas_limit(50000)
        .with_gas_price(0.0025)
    )
    return txn


def test_get_version(mock_cosmos_app):
    resp = mock_cosmos_app.get_version()

    assert resp.cla == 0
    assert resp.major == 2
    assert resp.minor == 18
    assert resp.patch == 0


def test_ins_get_public_key(mock_private_key, mock_cosmos_app):
    comparison_public_key = mock_private_key.to_public_key().to_hex()

    ledger_public_key = mock_cosmos_app.ins_get_addr_secp256k1("band").public_key.hex()

    assert ledger_public_key == comparison_public_key


def test_ins_get_addr(mock_private_key, mock_cosmos_app):
    comparison_public_key = mock_private_key.to_public_key()
    comparison_addr = comparison_public_key.to_address().to_acc_bech32()

    ledger_addr = mock_cosmos_app.ins_get_addr_secp256k1("band").address.decode()

    assert ledger_addr == comparison_addr


def test_sign_secp256k1(mock_private_key, mock_cosmos_app, mock_message):
    sign_doc = bytes(mock_message.get_sign_doc())

    comparison_signed_msg = mock_private_key.sign(sign_doc)

    data, remaining_data = remove_sequence(mock_cosmos_app.sign_secp256k1(sign_doc))
    r, c = remove_integer(data)
    s, _ = remove_integer(c)

    assert comparison_signed_msg == r.to_bytes(32, "big") + s.to_bytes(32, "big")
