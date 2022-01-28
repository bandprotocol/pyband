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


class CosmosTransactionServicer(CosmosTxServicerBase):
    def BroadcastTx(self, request: BroadcastTxRequest, context) -> BroadcastTxResponse:
        if (
            request
            == b"\n\x8d\x01\n\x8a\x01\n\x1c/cosmos.bank.v1beta1.MsgSend\x12j\n+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12+band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l\x1a\x0e\n\x05uband\x12\x0510000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@)!D8(|'\xad\xbd\x87\xa6\x14 K\x85\xf7\xfe\xd7S\xa4C\xb0\x8b\x8bB\t\xe9\xc1\xa6c\x82\xb5*x\xb4#@\xf2n\x15;\x82q\xf3\x01\xd4w\xc2.\xc4\x8f.I\xbc\x051\xb6q\xbd\x98g\xab\xec\xfb"
        ):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3278495,
                    txhash="B75F4352E285F6997237BAA5524165D531C97759EE39DE1B2C73E89C42762C3D",
                    data="0A1E0A1C2F636F736D6F732E62616E6B2E763162657461312E4D736753656E64",
                )
            )
        elif (
            request
            == b"\nd\nb\n\x1c/cosmos.bank.v1beta1.MsgSend\x12B\n\x03123\x12+band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l\x1a\x0e\n\x05uband\x12\x0510000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@~\xb6\x96Q\xd9\x0eU\xcfd>\r[\x96\x1d;\xf6\xb1\xcb\xbcp9\xf9\x98#\x06\x08bb\x88`\xe4\x84g\xd0\xbbq<\xdb\xa2\xf4\x8b\x84\xf7\xc6\xaf\x85\xa6\xd5\x1a\xe7\xd6\x82\xad\xc9I\xd7e\xb76\xb1\xed\x14\xdfi"
        ):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="6252299B8DF1A024F707E10B77627331FF9303CE0E6D6B3DC68F9CCB9BF742F9",
                    codespace="sdk",
                    code=7,
                    raw_log="Invalid sender address (decoding bech32 failed: invalid bech32 string length 3): invalid address",
                )
            )
        elif (
            request
            == b"\nd\nb\n\x1c/cosmos.bank.v1beta1.MsgSend\x12B\n+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12\x03123\x1a\x0e\n\x05uband\x12\x0510000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@\xf6]\x91:z\x8d\x18~\x95=4\xe75b\xce\xb6s\x93nM\xd1b\xec\x18\xa6#z\xd5/u\xf2\xddUPa\xd9\x83\x98~t)\xc0\xa2\xd0\xb6\xa5\x15\xf4\xea\x91\x9cr}\xbb\xef\xce+\x8aS\xef\x92\xe3\x19d"
        ):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="88588BCB2B8813E51EE5EC5DFBB831B37C5C9C5B6528BBC333D7E9AA49110194",
                    codespace="sdk",
                    code=7,
                    raw_log="Invalid recipient address (decoding bech32 failed: invalid bech32 string length 3): invalid address",
                )
            )
        elif (
            request
            == b"\n\x8e\x01\n\x8b\x01\n\x1c/cosmos.bank.v1beta1.MsgSend\x12k\n+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12+band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l\x1a\x0f\n\x05uband\x12\x06-10000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@\xd0\x0c;\xae\xb5\xf4\xee\xea\xce\xd5\xf5\xf3_v\x01\xa1\xdbF\rZ\xc3_J\xa5\xd2\x8d\xf8\xb6\xb4\xff\xe4\xd9qJB%A\t6\xd4\xedp\xd8\xd6\xaa2\xf0\x11\xd5\xaf\xfe\x9f\xcbz\x93@\x0f<\xa0\xcfJQ\x1a\xe8"
        ):
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
    tx_response = pyband_client.send_tx_block_mode(
        b"\n\x8d\x01\n\x8a\x01\n\x1c/cosmos.bank.v1beta1.MsgSend\x12j\n+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12+band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l\x1a\x0e\n\x05uband\x12\x0510000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@)!D8(|'\xad\xbd\x87\xa6\x14 K\x85\xf7\xfe\xd7S\xa4C\xb0\x8b\x8bB\t\xe9\xc1\xa6c\x82\xb5*x\xb4#@\xf2n\x15;\x82q\xf3\x01\xd4w\xc2.\xc4\x8f.I\xbc\x051\xb6q\xbd\x98g\xab\xec\xfb"
    )
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3278495,
            txhash="B75F4352E285F6997237BAA5524165D531C97759EE39DE1B2C73E89C42762C3D",
            data="0A1E0A1C2F636F736D6F732E62616E6B2E763162657461312E4D736753656E64",
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_invalid_sender(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        b"\nd\nb\n\x1c/cosmos.bank.v1beta1.MsgSend\x12B\n\x03123\x12+band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l\x1a\x0e\n\x05uband\x12\x0510000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@~\xb6\x96Q\xd9\x0eU\xcfd>\r[\x96\x1d;\xf6\xb1\xcb\xbcp9\xf9\x98#\x06\x08bb\x88`\xe4\x84g\xd0\xbbq<\xdb\xa2\xf4\x8b\x84\xf7\xc6\xaf\x85\xa6\xd5\x1a\xe7\xd6\x82\xad\xc9I\xd7e\xb76\xb1\xed\x14\xdfi"
    )
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
    tx_response = pyband_client.send_tx_block_mode(
        b"\nd\nb\n\x1c/cosmos.bank.v1beta1.MsgSend\x12B\n+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12\x03123\x1a\x0e\n\x05uband\x12\x0510000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@\xf6]\x91:z\x8d\x18~\x95=4\xe75b\xce\xb6s\x93nM\xd1b\xec\x18\xa6#z\xd5/u\xf2\xddUPa\xd9\x83\x98~t)\xc0\xa2\xd0\xb6\xa5\x15\xf4\xea\x91\x9cr}\xbb\xef\xce+\x8aS\xef\x92\xe3\x19d"
    )
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
    tx_response = pyband_client.send_tx_block_mode(
        b"\n\x8e\x01\n\x8b\x01\n\x1c/cosmos.bank.v1beta1.MsgSend\x12k\n+band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte\x12+band1d77h06hmw5r8gqh2nnf8msx48f3cc6rqt6pt8l\x1a\x0f\n\x05uband\x12\x06-10000\x12\x10\n\x08\x12\x04\n\x02\x08\x01\x18\x1e\x12\x04\x10\xc0\x9a\x0c\x1a@\xd0\x0c;\xae\xb5\xf4\xee\xea\xce\xd5\xf5\xf3_v\x01\xa1\xdbF\rZ\xc3_J\xa5\xd2\x8d\xf8\xb6\xb4\xff\xe4\xd9qJB%A\t6\xd4\xedp\xd8\xd6\xaa2\xf0\x11\xd5\xaf\xfe\x9f\xcbz\x93@\x0f<\xa0\xcfJQ\x1a\xe8"
    )
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="7E66D52CE4E39D2A730B2EB4EC15E8D0A923D861C895D3B208300E74A7C459CE",
            codespace="sdk",
            code=10,
            raw_log="-10000uband: invalid coins",
        )
    )

    assert tx_response == mock_result.tx_response
