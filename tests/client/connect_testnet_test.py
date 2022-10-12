import asyncio
import pytest
import pytest_asyncio
from pyband import Client


@pytest_asyncio.fixture(scope="module")
async def pyband_client():
    yield Client.from_endpoint("laozi-testnet6.bandchain.org", 443)


@pytest.fixture(scope="module")
def event_loop():
    """Change event_loop fixture to module level."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_get_chain_id(pyband_client):
    chain_id = await pyband_client.get_chain_id()
    assert chain_id == "band-laozi-testnet6"
