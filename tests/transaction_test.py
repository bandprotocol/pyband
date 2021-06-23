import pytest
from pyband.transaction import Transaction
from pyband.proto.oracle.v1.tx_pb2 import MsgRequestData

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.exceptions import EmptyMsgError, UndefinedError, ValueTooLargeError
from pyband.wallet import PrivateKey

MNEMONIC = "foo"
PRIVATE_KEY = PrivateKey.from_mnemonic(MNEMONIC)


def test_get_tx_data_msg_empty():
    t = Transaction().with_account_num(100).with_sequence(30).with_chain_id("bandchain")
    with pytest.raises(EmptyMsgError, match="message is empty"):
        t.get_tx_data(PRIVATE_KEY)


def test_get_tx_data_account_num_fail():
    t = (
        Transaction()
        .with_messages(
            MsgRequestData(
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
        )
        .with_sequence(30)
        .with_chain_id("bandchain")
    )
    with pytest.raises(UndefinedError, match="account_num should be defined"):
        t.get_tx_data(PRIVATE_KEY)


def test_get_tx_data_sequence_undefined():
    t = (
        Transaction()
        .with_messages(
            MsgRequestData(
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
        )
        .with_account_num(100)
        .with_chain_id("bandchain")
    )
    with pytest.raises(UndefinedError, match="sequence should be defined"):
        t.get_tx_data(PRIVATE_KEY)


def test_get_tx_data_chain_id_undefined():
    t = (
        Transaction()
        .with_messages(
            MsgRequestData(
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
        )
        .with_account_num(100)
        .with_sequence(30)
    )

    with pytest.raises(UndefinedError, match="chain_id should be defined"):
        t.get_tx_data(PRIVATE_KEY)


def test_get_tx_data_invalid_memo():
    t = (
        Transaction()
        .with_messages(
            MsgRequestData(
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
        )
        .with_account_num(100)
        .with_sequence(30)
        .with_chain_id("bandchain")
    )
    with pytest.raises(ValueTooLargeError, match="memo is too large"):
        t.with_memo(
            "This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world. This is the longest memo in the world.This is the longest memo in the world. This is the longest memo in the world.This is the longest memo in the world."
        )
