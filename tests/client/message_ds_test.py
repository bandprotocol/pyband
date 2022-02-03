import pytest
import grpc

from pyband.wallet import PrivateKey
from pyband.transaction import Transaction

# Servicers
from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import (
    ServiceServicer as CosmosTxServicerBase,
)


# Types
from pyband.proto.oracle.v1.tx_pb2 import MsgCreateDataSource, MsgEditDataSource

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
OWNER = "band1jea90wa0cvmw3k9pzz0lwh5sv4n07fe2r30wpk"
EXECUTABLE = b"\x00\x00\x00\x03BTC\x00\x00\x00\x00\x00\x00\x00\x01"

msg_create_ds_success = MsgCreateDataSource(
    name="CoinGecko",
    description="get symbol price from CoinGecko",
    sender=SENDER,
    owner=OWNER,
    treasury=OWNER,
    executable=EXECUTABLE,
)
msg_create_ds_empty_sender = MsgCreateDataSource(
    name="CoinGecko",
    description="get symbol price from CoinGecko",
    sender="",
    owner=OWNER,
    treasury=OWNER,
    executable=EXECUTABLE,
)
msg_create_ds_empty_owner = MsgCreateDataSource(
    name="CoinGecko",
    description="get symbol price from CoinGecko",
    sender=SENDER,
    owner="",
    treasury=OWNER,
    executable=EXECUTABLE,
)
msg_create_ds_empty_treasury = MsgCreateDataSource(
    name="CoinGecko",
    description="get symbol price from CoinGecko",
    sender=SENDER,
    owner=OWNER,
    treasury="",
    executable=EXECUTABLE,
)
msg_create_ds_empty_executable = MsgCreateDataSource(
    name="CoinGecko",
    description="get symbol price from CoinGecko",
    sender=SENDER,
    owner=OWNER,
    treasury="",
    executable=b"",
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
        if request.tx_bytes == getTxBytes(msg_create_ds_success):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3430969,
                    txhash="505629F67952FC13E8054D68AADE2D271668B5D649A52620834AB2BCACDC226F",
                    data="0A200A1E2F6F7261636C652E76312E4D736743726561746544617461536F75726365",
                )
            )
        elif request.tx_bytes == getTxBytes(msg_create_ds_empty_sender):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="AA94F71F54BA7DA97C00A3A810E40D2A19BDAF6580171A12AA0339348C02B228",
                    codespace="undefined",
                    code=1,
                    raw_log="internal",
                )
            )
        elif request.tx_bytes == getTxBytes(msg_create_ds_empty_owner):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="2C44B1DFF018E46D08B1AFFCAA098B6F7096401484D472CE24F213C290A992B9",
                    codespace="undefined",
                    code=1,
                    raw_log="internal",
                )
            )
        elif request.tx_bytes == getTxBytes(msg_create_ds_empty_treasury):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="AAF1DCCCA0CCBA39D43E66D5DF866BF34C93E02ADC56D26D8C00246D1F5173FE",
                    codespace="undefined",
                    code=1,
                    raw_log="internal",
                )
            )
        elif request.tx_bytes == getTxBytes(msg_create_ds_empty_executable):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="6488960EB0E8057B35D87D9C68F0904272A3DEBB31A55F3C8027DE81B8F83E90",
                    codespace="oracle",
                    code=20,
                    raw_log="empty executable",
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


def test_create_ds_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(getTxBytes(msg_create_ds_success))

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3430969,
            txhash="505629F67952FC13E8054D68AADE2D271668B5D649A52620834AB2BCACDC226F",
            data="0A200A1E2F6F7261636C652E76312E4D736743726561746544617461536F75726365",
        )
    )

    assert tx_response == mock_result.tx_response


def test_create_ds_empty_sender(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(msg_create_ds_empty_sender)
    )

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="AA94F71F54BA7DA97C00A3A810E40D2A19BDAF6580171A12AA0339348C02B228",
            codespace="undefined",
            code=1,
            raw_log="internal",
        )
    )

    assert tx_response == mock_result.tx_response


def test_create_ds_empty_owner(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(msg_create_ds_empty_owner)
    )

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="2C44B1DFF018E46D08B1AFFCAA098B6F7096401484D472CE24F213C290A992B9",
            codespace="undefined",
            code=1,
            raw_log="internal",
        )
    )

    assert tx_response == mock_result.tx_response


def test_create_ds_empty_treasury(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(msg_create_ds_empty_treasury)
    )

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="AAF1DCCCA0CCBA39D43E66D5DF866BF34C93E02ADC56D26D8C00246D1F5173FE",
            codespace="undefined",
            code=1,
            raw_log="internal",
        )
    )

    assert tx_response == mock_result.tx_response


def test_create_ds_empty_executable(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(msg_create_ds_empty_executable)
    )

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="6488960EB0E8057B35D87D9C68F0904272A3DEBB31A55F3C8027DE81B8F83E90",
            codespace="oracle",
            code=20,
            raw_log="empty executable",
        )
    )

    assert tx_response == mock_result.tx_response
