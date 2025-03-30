import pytest

from pyband.wallet import PrivateKey
from pyband.transaction import Transaction

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.cosmos.bank.v1beta1.tx_pb2 import MsgSend

# Servicer
from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import (
    ServiceServicer as CosmosTxServicerBase,
)

# Types
from pyband.proto.cosmos.tx.v1beta1.service_pb2 import (
    BroadcastTxRequest,
    BroadcastTxResponse,
)
from pyband.proto.cosmos.base.abci.v1beta1.abci_pb2 import TxResponse

MNEMONIC = "s"
PRIVATE_KEY = PrivateKey.from_mnemonic(MNEMONIC)
PUBLIC_KEY = PRIVATE_KEY.to_public_key()
ADDRESS = PUBLIC_KEY.to_address()
SENDER = ADDRESS.to_acc_bech32()

success_msg = MsgSend(
    from_address=SENDER,
    to_address="band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l",
    amount=[Coin(amount="10000", denom="uband")],
)
invalid_sender_msg = MsgSend(
    from_address="123",
    to_address="band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l",
    amount=[Coin(amount="10000", denom="uband")],
)
invalid_recipient_msg = MsgSend(
    from_address=SENDER,
    to_address="123",
    amount=[Coin(amount="10000", denom="uband")],
)
invalid_coins_msg = MsgSend(
    from_address=SENDER,
    to_address="band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l",
    amount=[Coin(amount="-10000", denom="uband")],
)


def getTxBytes(msg):
    t = (
        Transaction()
        .with_messages(msg)
        .with_account_num(100)
        .with_sequence(30)
        .with_chain_id("bandchain")
    )
    sign_doc = t.get_sign_doc()
    signature = PRIVATE_KEY.sign(sign_doc.SerializeToString())
    tx_raw_bytes = t.get_tx_data(signature)
    return tx_raw_bytes


class CosmosTransactionServicer(CosmosTxServicerBase):
    def BroadcastTx(self, request: BroadcastTxRequest, context) -> BroadcastTxResponse:
        if request.tx_bytes == getTxBytes(success_msg):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3278495,
                    txhash="B75F4352E285F6997237BAA5524165D531C97759EE39DE1B2C73E89C42762C3D",
                    data="0A1E0A1C2F636F736D6F732E62616E6B2E763162657461312E4D736753656E64",
                )
            )
        elif request.tx_bytes == getTxBytes(invalid_sender_msg):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="6252299B8DF1A024F707E10B77627331FF9303CE0E6D6B3DC68F9CCB9BF742F9",
                    codespace="sdk",
                    code=7,
                    raw_log="Invalid sender address (decoding bech32 failed: invalid bech32 string length 3): invalid address",
                )
            )
        elif request.tx_bytes == getTxBytes(invalid_recipient_msg):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="88588BCB2B8813E51EE5EC5DFBB831B37C5C9C5B6528BBC333D7E9AA49110194",
                    codespace="sdk",
                    code=7,
                    raw_log="Invalid recipient address (decoding bech32 failed: invalid bech32 string length 3): invalid address",
                )
            )
        elif request.tx_bytes == getTxBytes(invalid_coins_msg):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="7E66D52CE4E39D2A730B2EB4EC15E8D0A923D861C895D3B208300E74A7C459CE",
                    codespace="sdk",
                    code=10,
                    raw_log="-10000uband: invalid coins",
                )
            )


@pytest.fixture(scope="module")
def pyband_client(_grpc_server, grpc_addr):
    from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import (
        add_ServiceServicer_to_server as add_cosmos_tx,
    )

    add_cosmos_tx(CosmosTransactionServicer(), _grpc_server)

    _grpc_server.add_insecure_port(grpc_addr)
    _grpc_server.start()

    from pyband.client import Client

    yield Client(grpc_addr, insecure=True)
    _grpc_server.stop(grace=None)


def test_message_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(getTxBytes(success_msg))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3278495,
            txhash="B75F4352E285F6997237BAA5524165D531C97759EE39DE1B2C73E89C42762C3D",
            data="0A1E0A1C2F636F736D6F732E62616E6B2E763162657461312E4D736753656E64",
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_invalid_sender(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(getTxBytes(invalid_sender_msg))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="6252299B8DF1A024F707E10B77627331FF9303CE0E6D6B3DC68F9CCB9BF742F9",
            codespace="sdk",
            code=7,
            raw_log="Invalid sender address (decoding bech32 failed: invalid bech32 string length 3): invalid address",
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_invalid_recipient(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(getTxBytes(invalid_recipient_msg))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="88588BCB2B8813E51EE5EC5DFBB831B37C5C9C5B6528BBC333D7E9AA49110194",
            codespace="sdk",
            code=7,
            raw_log="Invalid recipient address (decoding bech32 failed: invalid bech32 string length 3): invalid address",
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_invalid_coins(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(getTxBytes(invalid_coins_msg))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="7E66D52CE4E39D2A730B2EB4EC15E8D0A923D861C895D3B208300E74A7C459CE",
            codespace="sdk",
            code=10,
            raw_log="-10000uband: invalid coins",
        )
    )

    assert tx_response == mock_result.tx_response
