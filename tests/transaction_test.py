import pytest
from google.protobuf.any_pb2 import Any

from pyband.exceptions import EmptyMsgError, UndefinedError, ValueTooLargeError
from pyband.transaction import Transaction
from pyband.wallet import PrivateKey

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.cosmos.tx.v1beta1.tx_pb2 import Fee, SignDoc
from pyband.proto.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest, QueryAccountResponse
from pyband.proto.oracle.v1.tx_pb2 import MsgRequestData

# Servicers
from pyband.proto.cosmos.auth.v1beta1.query_pb2_grpc import QueryServicer as QueryServicerBase


MNEMONIC = "s"
PRIVATE_KEY = PrivateKey.from_mnemonic(MNEMONIC)
PUBLIC_KEY = PRIVATE_KEY.to_public_key()
ADDRESS = PUBLIC_KEY.to_address()
SENDER = ADDRESS.to_acc_bech32()


class QueryServicer(QueryServicerBase):
    def Account(self, request: QueryAccountRequest, context):
        return QueryAccountResponse(
            account=Any(
                type_url="/cosmos.auth.v1beta1.BaseAccount",
                value=b"\n+band1z2hwz2vn6ardpjzgfx2k3wh2zglknwavhw3v2r\022F\n\037/cosmos.crypto.secp256k1.PubKey\022#\n!\002\243\357\354\271\2712\330H\300F\342suhP\357^!\007\244&\365\t\314\274\312\034~\240\004A\341\030h \010",
            )
        )


@pytest.fixture(scope="module")
def pyband_client(_grpc_server, grpc_addr):
    from pyband.proto.cosmos.auth.v1beta1.query_pb2_grpc import add_QueryServicer_to_server as add_cosmos_query

    add_cosmos_query(QueryServicer(), _grpc_server)

    _grpc_server.add_insecure_port(grpc_addr)
    _grpc_server.start()

    from pyband.client import Client

    yield Client(grpc_addr, insecure=True)
    _grpc_server.stop(grace=None)


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
        body_bytes=b"\n\204\001\n\031/oracle.v1.MsgRequestData\022g\010\001\022\017\000\000\000\003BTC\000\000\000\000\000\000\000\001\030\004 \003*\013from_pyband2\014\n\005uband\022\0031008\260\352\001@\320\206\003J+band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        auth_info_bytes=b"\nP\nF\n\037/cosmos.crypto.secp256k1.PubKey\022#\n!\003\376p\213\332fRO\322\306\274\351\006\202\343\205U\250Q\340=*\356Ob\233\005\336\220\365\036\331\274\022\004\n\002\010\001\030\036\022\004\020\300\232\014",
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
        body_bytes=b"\n\204\001\n\031/oracle.v1.MsgRequestData\022g\010\001\022\017\000\000\000\003BTC\000\000\000\000\000\000\000\001\030\004 \003*\013from_pyband2\014\n\005uband\022\0031008\260\352\001@\320\206\003J+band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        auth_info_bytes=b"\n\010\022\004\n\002\010\001\030\036\022\004\020\300\232\014",
        chain_id="bandchain",
        account_number=100,
    )


def test_get_sign_data_with_sender_success(pyband_client):
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

    t = (
        Transaction()
        .with_messages(msg)
        .with_sender(pyband_client, "band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c")
        .with_chain_id("bandchain")
        .with_gas(50000)
        .with_fee(fee)
    )
    assert t.get_sign_doc(PUBLIC_KEY) == SignDoc(
        body_bytes=b"\n\204\001\n\031/oracle.v1.MsgRequestData\022g\010\001\022\017\000\000\000\003BTC\000\000\000\000\000\000\000\001\030\004 \003*\013from_pyband2\014\n\005uband\022\0031008\260\352\001@\320\206\003J+band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        auth_info_bytes=b"\nP\nF\n\037/cosmos.crypto.secp256k1.PubKey\022#\n!\003\376p\213\332fRO\322\306\274\351\006\202\343\205U\250Q\340=*\356Ob\233\005\336\220\365\036\331\274\022\004\n\002\010\001\030\010\022\020\n\n\n\005uband\022\0010\020\320\206\003",
        chain_id="bandchain",
        account_number=104,
    )


def test_create_transaction_with_sender_fail(pyband_client):
    with pytest.raises(EmptyMsgError, match="messsage is empty, please use with_messages at least 1 message"):
        t = Transaction().with_sender(pyband_client, "band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c")


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
    assert (
        tx_raw_bytes
        == b"\n\x87\x01\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyband2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12X\nP\nF\n\x1f/cosmos.crypto.secp256k1.PubKey\x12#\n!\x03\xfep\x8b\xdafRO\xd2\xc6\xbc\xe9\x06\x82\xe3\x85U\xa8Q\xe0=*\xeeOb\x9b\x05\xde\x90\xf5\x1e\xd9\xbc\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@/\xa2\xe7\xb3e\xf8\x13\x7f$\x162q\x11\xbaX\xa0\x93\xbeWeO\xc7~\x0e3\xe5F\xd0\xbd\xf1\xd5\xe1k\xefnxuv\x14l?\x8a3\x06Z_7\x93\xd7\xcc\xbf\xc0\xa2S\xff\xaa\x19\xfd}\xddO\xe3\xd9\xb1"
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
    assert (
        tx_raw_bytes
        == b"\n\x87\x01\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyband2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@/\xa2\xe7\xb3e\xf8\x13\x7f$\x162q\x11\xbaX\xa0\x93\xbeWeO\xc7~\x0e3\xe5F\xd0\xbd\xf1\xd5\xe1k\xefnxuv\x14l?\x8a3\x06Z_7\x93\xd7\xcc\xbf\xc0\xa2S\xff\xaa\x19\xfd}\xddO\xe3\xd9\xb1"
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
    assert (
        tx_raw_bytes
        == b'\n\x87\x01\n\x84\x01\n\x19/oracle.v1.MsgRequestData\x12g\x08\x01\x12\x0f\x00\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01\x18\x04 \x03*\x0bfrom_pyband2\x0c\n\x05uband\x12\x031008\xb0\xea\x01@\xd0\x86\x03J+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@\xf3\xb5z\xa4\xea\xc6\x02\xff\\\x862x\x80\xba\xbf\xd8%t\x88X\xddrDY^"C\xd7\x9c\xf1\xb3\xbe]\xe7Z\x9a\x07\xedX\xf7r\xd4\xf8\x044\xf8\xda\x86\x80(~J\xb8\r\x12\x03\x17\xcb\x9f\xb95\xa4&\xa1'
    )
