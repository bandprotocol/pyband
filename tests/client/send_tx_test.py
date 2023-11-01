import asyncio

import pytest
import pytest_asyncio
from grpclib.testing import ChannelFor

from pyband import Client
from pyband.proto.cosmos.base.abci.v1beta1 import TxResponse, AbciMessageLog, StringEvent, Attribute
from pyband.proto.cosmos.tx.v1beta1 import BroadcastTxRequest, BroadcastTxResponse
from pyband.proto.cosmos.tx.v1beta1 import ServiceBase as CosmosTxServiceBase


# Note: Success, if code = 0
class CosmosTransactionService(CosmosTxServiceBase):
    async def broadcast_tx(self, broadcast_tx_request: BroadcastTxRequest) -> BroadcastTxResponse:
        if broadcast_tx_request.tx_bytes == b"async_any_hash":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="txhash",
                )
            )
        elif broadcast_tx_request.tx_bytes == b"sync_success":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="6E9A3A8145A0A6562AAE4A4066125006A392620A5656E3CCB145C22FF3CC8AA0",
                    raw_log="[]",
                )
            )
        elif broadcast_tx_request.tx_bytes == b"sync_fail_wrong_bytes":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="C278EC5A69C34AACE42773E41B1163E6CE40C906F2A14F807D39D1B2A1C2DFF5",
                    codespace="sdk",
                    code=2,
                    raw_log='errUnknownField "*tx.TxRaw": {TagNum: 13, WireType:"bytes"}: tx parse error',
                )
            )


@pytest_asyncio.fixture(scope="module")
async def pyband_client():
    channel_for = ChannelFor(services=[CosmosTransactionService()])
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


# Async mode: returns immediately (transaction might fail)
# send any bytes value -> will result in response txhash
@pytest.mark.asyncio
async def test_send_tx_async_mode_success(pyband_client):
    tx_response = await pyband_client.send_tx_async_mode(b"async_any_hash")
    mock_result = TxResponse(
        txhash="txhash",
    )
    assert tx_response == mock_result


@pytest.mark.asyncio
async def test_send_tx_async_mode_invalid_input(pyband_client):
    with pytest.raises(TypeError):
        await pyband_client.send_tx_async_mode(1)


# Sync mode: wait for checkTx execution response
# Success if code = 0
@pytest.mark.asyncio
async def test_send_tx_sync_mode_success(pyband_client):
    tx_response = await pyband_client.send_tx_sync_mode(b"sync_success")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="6E9A3A8145A0A6562AAE4A4066125006A392620A5656E3CCB145C22FF3CC8AA0",
            raw_log="[]",
        )
    )
    assert tx_response == mock_result.tx_response


# Fail if code != 0, invalid bytes code = 2
@pytest.mark.asyncio
async def test_send_tx_sync_mode_invalid_bytes(pyband_client):
    tx_response = await pyband_client.send_tx_sync_mode(b"sync_fail_wrong_bytes")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="C278EC5A69C34AACE42773E41B1163E6CE40C906F2A14F807D39D1B2A1C2DFF5",
            codespace="sdk",
            code=2,
            raw_log='errUnknownField "*tx.TxRaw": {TagNum: 13, WireType:"bytes"}: tx parse error',
        )
    )
    assert tx_response == mock_result.tx_response


@pytest.mark.asyncio
async def test_send_tx_sync_mode_invalid_input(pyband_client):
    with pytest.raises(TypeError):
        await pyband_client.send_tx_sync_mode(1)
