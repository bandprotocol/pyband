import asyncio

import pytest
import pytest_asyncio
from betterproto.lib.google.protobuf import Any
from grpclib.testing import ChannelFor

from pyband import Client
from pyband.exceptions import EmptyMsgError, UndefinedError, ValueTooLargeError
from pyband.messages.oracle.v1 import MsgRequestData
from pyband.proto.cosmos.auth.v1beta1 import QueryAccountRequest, QueryAccountResponse
from pyband.proto.cosmos.auth.v1beta1 import QueryBase as CosmosAuthServiceBase
from pyband.proto.cosmos.base.v1beta1 import Coin
from pyband.proto.cosmos.tx.v1beta1 import SignDoc
from pyband.transaction import Transaction
from pyband.wallet import PrivateKey

MNEMONIC = "s"
PRIVATE_KEY = PrivateKey.from_mnemonic(MNEMONIC)
PUBLIC_KEY = PRIVATE_KEY.to_public_key()
ADDRESS = PUBLIC_KEY.to_address()
SENDER = ADDRESS.to_acc_bech32()


class AuthService(CosmosAuthServiceBase):
    async def account(self, query_accounts_request: QueryAccountRequest):
        return QueryAccountResponse(
            account=Any(
                type_url="/cosmos.auth.v1beta1.BaseAccount",
                value=b"\n+band1z2hwz2vn6ardpjzgfx2k3wh2zglknwavhw3v2r\022F\n\037/cosmos.crypto.secp256k1.PubKey\022#\n!\002\243\357\354\271\2712\330H\300F\342suhP\357^!\007\244&\365\t\314\274\312\034~\240\004A\341\030h \010",
            )
        )


@pytest_asyncio.fixture(scope="module")
async def pyband_client():
    channel_for = ChannelFor(services=[AuthService()])
    channel = await channel_for.__aenter__()
    yield Client(channel)
    channel.close()


@pytest.fixture(scope="module")
def event_loop():
    """Change event_loop fixture to module level."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


def test_get_sign_doc_success():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender="band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_sequence(30).with_chain_id("bandchain")
    assert t.get_sign_doc(PUBLIC_KEY) == SignDoc(
        body_bytes=b"\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyband2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        auth_info_bytes=b"\nP\nF\n\x1f/cosmos.crypto.secp256k1.PubKey\x12#\n!\x03\xfep\x8b\xdafRO\xd2\xc6\xbc\xe9\x06\x82\xe3\x85U\xa8Q\xe0=*\xeeOb\x9b\x05\xde\x90\xf5\x1e\xd9\xbc\x12\x04\n\x02\x08\x01\x18\x1e\x12\x12\n\x0c\n\x05uband\x12\x03500\x10\xc0\x9a\x0c",
        chain_id="bandchain",
        account_number=100,
    )


def test_get_sign_doc_no_public_key_success():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender="band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_sequence(30).with_chain_id("bandchain")
    assert t.get_sign_doc() == SignDoc(
        body_bytes=b"\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyband2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        auth_info_bytes=b"\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x12\n\x0c\n\x05uband\x12\x03500\x10\xc0\x9a\x0c",
        chain_id="bandchain",
        account_number=100,
    )


@pytest.mark.asyncio
async def test_get_sign_data_with_sender_success(pyband_client):
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender="band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
    )
    fee = [Coin(amount="0", denom="uband")]

    t = Transaction().with_messages(msg).with_chain_id("bandchain").with_gas_limit(50000)
    await t.with_sender(pyband_client, "band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c")

    assert t.get_sign_doc(PUBLIC_KEY) == SignDoc(
        body_bytes=b"\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyband2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        auth_info_bytes=b"\nP\nF\n\x1f/cosmos.crypto.secp256k1.PubKey\x12#\n!\x03\xfep\x8b\xdafRO\xd2\xc6\xbc\xe9\x06\x82\xe3\x85U\xa8Q\xe0=*\xeeOb\x9b\x05\xde\x90\xf5\x1e\xd9\xbc\x12\x04\n\x02\x08\x01\x18\x08\x12\x12\n\x0c\n\x05uband\x12\x03125\x10\xd0\x86\x03",
        chain_id="bandchain",
        account_number=104,
    )


@pytest.mark.asyncio
async def test_create_transaction_with_sender_fail(pyband_client):
    with pytest.raises(EmptyMsgError, match="message is empty, please use with_messages at least 1 message"):
        await Transaction().with_sender(pyband_client, "band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c")


def test_get_sign_doc_msg_empty():
    t = Transaction().with_account_num(100).with_sequence(30).with_chain_id("bandchain")
    with pytest.raises(EmptyMsgError, match="message is empty"):
        t.get_sign_doc(PUBLIC_KEY)


def test_get_sign_doc_account_num_fail():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender="band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
    )

    t = Transaction().with_messages(msg).with_sequence(30).with_chain_id("bandchain")
    with pytest.raises(UndefinedError, match="account_num should be defined"):
        t.get_sign_doc(PUBLIC_KEY)


def test_get_sign_doc_sequence_undefined():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender="band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_chain_id("bandchain")
    with pytest.raises(UndefinedError, match="sequence should be defined"):
        t.get_sign_doc(PUBLIC_KEY)


def test_get_sign_doc_chain_id_undefined():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender="band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_sequence(30)

    with pytest.raises(UndefinedError, match="chain_id should be defined"):
        t.get_sign_doc(PUBLIC_KEY)


def test_invalid_memo():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender="band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_sequence(30).with_chain_id("bandchain")
    with pytest.raises(ValueTooLargeError, match="memo is too large"):
        t.with_memo(
            "This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world.This is the longest memo in the world. This is the longest memo in the world.This is the longest memo in the world."
        )


def test_get_tx_data_success():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender=SENDER,
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_sequence(30).with_chain_id("bandchain")

    sign_doc = t.get_sign_doc(PUBLIC_KEY)
    signature = PRIVATE_KEY.sign(sign_doc.SerializeToString())
    tx_raw_bytes = t.get_tx_data(signature, PUBLIC_KEY)
    assert tx_raw_bytes == (
        b"\n\x87\x01\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00"
        b"\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyb"
        b"and2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band1jrhuqrymzt4m"
        b"nvgw8cvy3s9zhx3jj0dq30qpte\x12f\nP\nF\n\x1f/cosmos.crypto.secp256k1.PubKe"
        b"y\x12#\n!\x03\xfep\x8b\xdafRO\xd2\xc6\xbc\xe9\x06\x82\xe3\x85U\xa8Q"
        b"\xe0=*\xeeOb\x9b\x05\xde\x90\xf5\x1e\xd9\xbc\x12\x04\n\x02\x08\x01"
        b"\x18\x1e\x12\x12\n\x0c\n\x05uband\x12\x03500\x10\xc0\x9a\x0c\x1a@\xfbPZh"
        b"\xc4\x8al9\t\x99\xbdq\xbd5R\x0c\xc0\x91\xff7\x03\x8f\xde\x81\xe6\x96\x84\x8f"
        b"I03&f|#\x91\xbaK\x01\x9c\x94\x04r\x94wg\xcfc\x0cQ\x03\xffp>\x1a]"
        b"\xcb\xd0\x08\x7fo \x90\x82"
    )


def test_get_tx_data_tx_raw_bytes_no_public_key_success():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender=SENDER,
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_sequence(30).with_chain_id("bandchain")

    sign_doc = t.get_sign_doc(PUBLIC_KEY)
    signature = PRIVATE_KEY.sign(sign_doc.SerializeToString())
    tx_raw_bytes = t.get_tx_data(signature)
    assert tx_raw_bytes == (
        b"\n\x87\x01\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00"
        b"\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyb"
        b"and2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band1jrhuqrymzt4m"
        b"nvgw8cvy3s9zhx3jj0dq30qpte\x12\x1e\n\x08\x12\x04\n\x02\x08\x01"
        b"\x18\x1e\x12\x12\n\x0c\n\x05uband\x12\x03500\x10\xc0\x9a\x0c\x1a@\xfbPZh"
        b"\xc4\x8al9\t\x99\xbdq\xbd5R\x0c\xc0\x91\xff7\x03\x8f\xde\x81\xe6\x96\x84\x8f"
        b"I03&f|#\x91\xbaK\x01\x9c\x94\x04r\x94wg\xcfc\x0cQ\x03\xffp>\x1a]"
        b"\xcb\xd0\x08\x7fo \x90\x82"
    )


def test_get_tx_data_no_public_key_success():
    msg = MsgRequestData(
        oracle_script_id=1,
        calldata=bytes.fromhex("000000034254430000000000000001"),
        ask_count=4,
        min_count=3,
        client_id="from_pyband",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=30000,
        execute_gas=50000,
        sender=SENDER,
    )

    t = Transaction().with_messages(msg).with_account_num(100).with_sequence(30).with_chain_id("bandchain")

    sign_doc = t.get_sign_doc()
    signature = PRIVATE_KEY.sign(sign_doc.SerializeToString())
    tx_raw_bytes = t.get_tx_data(signature)
    assert tx_raw_bytes == (
        b"\n\x87\x01\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00"
        b"\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyb"
        b"and2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band1jrhuqrymzt4m"
        b"nvgw8cvy3s9zhx3jj0dq30qpte\x12\x1e\n\x08\x12\x04\n\x02\x08\x01"
        b"\x18\x1e\x12\x12\n\x0c\n\x05uband\x12\x03500\x10\xc0\x9a\x0c\x1a@"
        b"\xd3\x84\xa1\xbc\xdb\x07\xbe\xd5\xf5\xa3\x95w.\xe1\xa3\xab0t\xc4\xcb"
        b"\xb5\xb7\xeb1\x86\xc8>=\xf4&\x99CmdU\x1f\xe8\x18\x11<\x9a\xfd\xf4\xf8"
        b"\x18\x8f>\xba\x8dzZ\xdfq\xe8\x88i\x92c3\xab_\x90\xc6\x8d"
    )
