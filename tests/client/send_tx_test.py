import pytest

# Servicer
from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import ServiceServicer as CosmosTxServicerBase

# Types
from pyband.proto.cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest, BroadcastTxResponse
from pyband.proto.cosmos.base.abci.v1beta1.abci_pb2 import TxResponse
from pyband.proto.tendermint.abci.types_pb2 import RequestCheckTx, ResponseCheckTx

# Google
from google.protobuf.any_pb2 import Any

# Success, if code = 0
class CosmosTransactionServicer(CosmosTxServicerBase):
    def BroadcastTx(self, request: BroadcastTxRequest, context) -> BroadcastTxResponse:
        if request.tx_bytes == b"async_any_hash":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="txhash",
                )
            )
        elif request.tx_bytes == b"sync_success":
            return BroadcastTxResponse(
                tx_response=TxResponse(txhash="txhash", codespace="sdk", code=0, raw_log="Success")
            )
        elif request.tx_bytes == b"sync_fail":
            return BroadcastTxResponse(
                tx_response=TxResponse(txhash="txhash", codespace="sdk", code=5, raw_log="Fail")
            )
        elif request.tx_bytes == b"sync_fail_wrong_bytes":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="C278EC5A69C34AACE42773E41B1163E6CE40C906F2A14F807D39D1B2A1C2DFF5",
                    codespace="sdk",
                    code=2,
                    raw_log='errUnknownField "*tx.TxRaw": {TagNum: 13, WireType:"bytes"}: tx parse error',
                )
            )
        elif request.tx_bytes == b"block_success":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="CC06ABAE35591E6668451D9B05D04A0E0C4257A582E4D714975363260A092233",
                    codespace="sdk",
                    code=0,
                    raw_log="Success",
                    gas_wanted=5000000,
                    gas_used=21747,
                )
            )
        elif request.tx_bytes == b"block_fail":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="CC06ABAE35591E6668451D9B05D04A0E0C4257A582E4D714975363260A092233",
                    codespace="sdk",
                    code=5,
                    raw_log="0uband, is smaller than 9000000uband: insufficient funds: insufficient funds",
                    gas_wanted=5000000,
                    gas_used=21747,
                )
            )
        elif request.tx_bytes == b"block_fail_wrong_bytes":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="7CA12506E88CF8B814E20848B229460F91FC0370C44A7C4FEE786960CE30C36D",
                    codespace="sdk",
                    code=2,
                    raw_log='errUnknownField "*tx.TxRaw": {TagNum: 14, WireType:"start_group"}: tx parse error',
                    gas_used=6429,
                )
            )


@pytest.fixture(scope="module")
def pyband_client(_grpc_server, grpc_addr):
    from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import add_ServiceServicer_to_server as add_cosmos_tx

    add_cosmos_tx(CosmosTransactionServicer(), _grpc_server)

    _grpc_server.add_insecure_port(grpc_addr)
    _grpc_server.start()

    from pyband.client import Client

    yield Client(grpc_addr)
    _grpc_server.stop(grace=None)


# Async mode: returns immediately (transaction might fail)
# send any bytes value -> will result in response txhash
def test_send_tx_async_mode_success(pyband_client):
    tx_response = pyband_client.send_tx_async_mode(b"async_any_hash")
    mock_result = TxResponse(
        txhash="txhash",
    )
    assert tx_response == mock_result


def test_send_tx_async_mode_invalid_input(pyband_client):
    tx_response = pyband_client.send_tx_async_mode(1)
    assert tx_response == None


# Sync mode: wait for checkTx execution response
# Success if code = 0
def test_send_tx_sync_mode_success(pyband_client):
    tx_response = pyband_client.send_tx_sync_mode(b"sync_success")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(txhash="txhash", codespace="sdk", code=0, raw_log="Success")
    )
    assert tx_response == mock_result.tx_response


# Fail if code != 0, invalid bytes code = 2
def test_send_tx_sync_mode_invalid_bytes(pyband_client):
    tx_response = pyband_client.send_tx_sync_mode(b"sync_fail_wrong_bytes")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="C278EC5A69C34AACE42773E41B1163E6CE40C906F2A14F807D39D1B2A1C2DFF5",
            codespace="sdk",
            code=2,
            raw_log='errUnknownField "*tx.TxRaw": {TagNum: 13, WireType:"bytes"}: tx parse error',
        )
    )
    assert tx_response == mock_result.tx_response


# Fail if code != 0
def test_send_tx_sync_mode_fai(pyband_client):
    tx_response = pyband_client.send_tx_sync_mode(b"sync_fail")
    mock_result = BroadcastTxResponse(tx_response=TxResponse(txhash="txhash", codespace="sdk", code=5, raw_log="Fail"))
    assert tx_response == mock_result.tx_response


def test_send_tx_sync_mode_invalid_input(pyband_client):
    tx_response = pyband_client.send_tx_sync_mode(1)
    assert tx_response == None


# Block mode: wait for tx to be committed to a block
# Success if code = 0
def test_send_tx_block_mode_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(b"block_success")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="CC06ABAE35591E6668451D9B05D04A0E0C4257A582E4D714975363260A092233",
            codespace="sdk",
            code=0,
            raw_log="Success",
            gas_wanted=5000000,
            gas_used=21747,
        )
    )
    assert tx_response == mock_result.tx_response


# Fail if code != 0
def test_send_tx_block_mode_fail(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(b"block_fail")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="CC06ABAE35591E6668451D9B05D04A0E0C4257A582E4D714975363260A092233",
            codespace="sdk",
            code=5,
            raw_log="0uband, is smaller than 9000000uband: insufficient funds: insufficient funds",
            gas_wanted=5000000,
            gas_used=21747,
        )
    )
    assert tx_response == mock_result.tx_response


# Fail if code != 0, invalid bytes code = 2
def test_send_tx_block_mode_invalid_bytes(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(b"block_fail_wrong_bytes")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="7CA12506E88CF8B814E20848B229460F91FC0370C44A7C4FEE786960CE30C36D",
            codespace="sdk",
            code=2,
            raw_log='errUnknownField "*tx.TxRaw": {TagNum: 14, WireType:"start_group"}: tx parse error',
            gas_used=6429,
        )
    )
    assert tx_response == mock_result.tx_response


def test_send_tx_block_mode_invalid_input(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(1)
    assert tx_response == None
