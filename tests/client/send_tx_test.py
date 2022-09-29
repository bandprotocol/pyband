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
        elif broadcast_tx_request.tx_bytes == b"block_success":
            return block_mode_success_result
        elif broadcast_tx_request.tx_bytes == b"block_out_of_gas":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=1284491,
                    txhash="2CE53A417435AD62F14C27535E19E6B5B2B0FDBF4CDC3532148DAE29BE5666BE",
                    codespace="sdk",
                    code=11,
                    raw_log="out of gas in location: PER_VALIDATOR_REQUEST_FEE; gasWanted: 200000, gasUsed: 517238: out of gas",
                    gas_wanted=200000,
                    gas_used=517238,
                )
            )
        elif broadcast_tx_request.tx_bytes == b"block_fail":
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
        elif broadcast_tx_request.tx_bytes == b"block_fail_wrong_bytes":
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="7CA12506E88CF8B814E20848B229460F91FC0370C44A7C4FEE786960CE30C36D",
                    codespace="sdk",
                    code=2,
                    raw_log='errUnknownField "*tx.TxRaw": {TagNum: 14, WireType:"start_group"}: tx parse error',
                    gas_used=6429,
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


# Block mode: wait for tx to be committed to a block
@pytest.mark.asyncio
async def test_send_tx_block_mode_success(pyband_client):
    tx_response = await pyband_client.send_tx_block_mode(b"block_success")
    mock_result = block_mode_success_result.tx_response
    assert tx_response == mock_result


@pytest.mark.asyncio
async def test_send_tx_block_mode_out_of_gas(pyband_client):
    tx_response = await pyband_client.send_tx_block_mode(b"block_out_of_gas")
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=1284491,
            txhash="2CE53A417435AD62F14C27535E19E6B5B2B0FDBF4CDC3532148DAE29BE5666BE",
            codespace="sdk",
            code=11,
            raw_log="out of gas in location: PER_VALIDATOR_REQUEST_FEE; gasWanted: 200000, gasUsed: 517238: out of gas",
            gas_wanted=200000,
            gas_used=517238,
        )
    )
    assert tx_response == mock_result.tx_response


# Fail if code != 0
@pytest.mark.asyncio
async def test_send_tx_block_mode_fail(pyband_client):
    tx_response = await pyband_client.send_tx_block_mode(b"block_fail")
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
@pytest.mark.asyncio
async def test_send_tx_block_mode_invalid_bytes(pyband_client):
    tx_response = await pyband_client.send_tx_block_mode(b"block_fail_wrong_bytes")
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


@pytest.mark.asyncio
async def test_send_tx_block_mode_invalid_input(pyband_client):
    with pytest.raises(TypeError):
        await pyband_client.send_tx_block_mode(1)


block_mode_success_result = BroadcastTxResponse(
    tx_response=TxResponse(
        height=1285934,
        txhash="767353B21A770E7D02E71BDCDD75AB5AB3F60E86CB4633A1BE49BEECA8A8CE4E",
        data="0A090A0772657175657374",
        raw_log="[{'events':[{'type':'message','attributes':[{'key':'action','value':'request'}]},{'type':'raw_request','attributes':[{'key':'data_source_id','value':'61'},{'key':'data_source_hash','value':'07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef'},{'key':'external_id','value':'6'},{'key':'calldata','value':'ETH'},{'key':'data_source_id','value':'57'},{'key':'data_source_hash','value':'61b369daa5c0918020a52165f6c7662d5b9c1eee915025cb3d2b9947a26e48c7'},{'key':'external_id','value':'0'},{'key':'calldata','value':'ETH'},{'key':'data_source_id','value':'62'},{'key':'data_source_hash','value':'107048da9dbf7960c79fb20e0585e080bb9be07d42a1ce09c5479bbada8d0289'},{'key':'external_id','value':'3'},{'key':'calldata','value':'ETH'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'5'},{'key':'calldata','value':'huobipro ETH'},{'key':'data_source_id','value':'59'},{'key':'data_source_hash','value':'5c011454981c473af3bf6ef93c76b36bfb6cc0ce5310a70a1ba569de3fc0c15d'},{'key':'external_id','value':'2'},{'key':'calldata','value':'ETH'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'4'},{'key':'calldata','value':'binance ETH'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'9'},{'key':'calldata','value':'bittrex ETH'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'7'},{'key':'calldata','value':'kraken ETH'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'8'},{'key':'calldata','value':'bitfinex ETH'},{'key':'data_source_id','value':'58'},{'key':'data_source_hash','value':'7e6759fade717a06fb643392bfde837bfc3437da2ded54feed706e6cd35de461'},{'key':'external_id','value':'1'},{'key':'calldata','value':'ETH'}]},{'type':'request','attributes':[{'key':'id','value':'287004'},{'key':'client_id','value':'Blue'},{'key':'oracle_script_id','value':'37'},{'key':'calldata','value':'00000001000000034554480000000000000064'},{'key':'ask_count','value':'16'},{'key':'min_count','value':'10'},{'key':'gas_used','value':'71512'},{'key':'validator','value':'bandvaloper18tjynh8v0kvf9lmjenx02fgltxk0c6jmm2wcjc'},{'key':'validator','value':'bandvaloper1w46umthap3cmvqarrznauy25mdhqu45tv8hq62'},{'key':'validator','value':'bandvaloper1qudzmeu5yr7ryaq9spfpurptvlv4mxehe8x86e'},{'key':'validator','value':'bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa'},{'key':'validator','value':'bandvaloper1npezmz5cw208gm7l7nhay5xm6h5k4we5axn663'},{'key':'validator','value':'bandvaloper1d0kcwzukkjl2w2nty3xerqpy3ypdrph67hxx4v'},{'key':'validator','value':'bandvaloper19j74weeme5ehvmfnduz5swkxysz4twg92swxaf'},{'key':'validator','value':'bandvaloper1ejnk6k8ny3y5kwr234m3y32p7dxsx2a0wvcpyl'},{'key':'validator','value':'bandvaloper185sr49ntmfzfc5z52eh0z5m2vjvahwqa6qvk27'},{'key':'validator','value':'bandvaloper106e65xpz88s5xvnlp5lqx98th9zvpptu7uj7zy'},{'key':'validator','value':'bandvaloper12dzdxtd2mtnc37nfutwmj0lv8lsfgn6um0e5q5'},{'key':'validator','value':'bandvaloper1h52l9shahsdzrduwtjt9exc349sehx4s2zydrv'},{'key':'validator','value':'bandvaloper1u3c40nglllu4upuddlz6l59afq7uuz7lq6z977'},{'key':'validator','value':'bandvaloper1g4tfgzuxtnfzpnc7drk83n6r6ghkmzwsc7eglq'},{'key':'validator','value':'bandvaloper1kfj48adjsnrgu83lau6wc646q2uf65rf84tzus'},{'key':'validator','value':'bandvaloper1t0x8dv4frjnrnl0geegf9l5hrj9wa7qwmjrrwg'}]}]}]",
        logs=[
            AbciMessageLog(
                events=[
                    StringEvent(type="message", attributes=[Attribute(key="action", value="request")]),
                    StringEvent(
                        type="raw_request",
                        attributes=[
                            Attribute(key="data_source_id", value="61"),
                            Attribute(
                                key="data_source_hash",
                                value="07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef",
                            ),
                            Attribute(key="external_id", value="6"),
                            Attribute(key="calldata", value="ETH"),
                            Attribute(key="data_source_id", value="57"),
                            Attribute(
                                key="data_source_hash",
                                value="61b369daa5c0918020a52165f6c7662d5b9c1eee915025cb3d2b9947a26e48c7",
                            ),
                            Attribute(key="external_id", value="0"),
                            Attribute(key="calldata", value="ETH"),
                            Attribute(key="data_source_id", value="62"),
                            Attribute(
                                key="data_source_hash",
                                value="107048da9dbf7960c79fb20e0585e080bb9be07d42a1ce09c5479bbada8d0289",
                            ),
                            Attribute(key="external_id", value="3"),
                            Attribute(key="calldata", value="ETH"),
                            Attribute(key="data_source_id", value="60"),
                            Attribute(
                                key="data_source_hash",
                                value="2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac",
                            ),
                            Attribute(key="external_id", value="5"),
                            Attribute(key="calldata", value="huobipro ETH"),
                            Attribute(key="data_source_id", value="59"),
                            Attribute(
                                key="data_source_hash",
                                value="5c011454981c473af3bf6ef93c76b36bfb6cc0ce5310a70a1ba569de3fc0c15d",
                            ),
                            Attribute(key="external_id", value="2"),
                            Attribute(key="calldata", value="ETH"),
                            Attribute(key="data_source_id", value="60"),
                            Attribute(
                                key="data_source_hash",
                                value="2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac",
                            ),
                            Attribute(key="external_id", value="4"),
                            Attribute(key="calldata", value="binance ETH"),
                            Attribute(key="data_source_id", value="60"),
                            Attribute(
                                key="data_source_hash",
                                value="2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac",
                            ),
                            Attribute(key="external_id", value="9"),
                            Attribute(key="calldata", value="bittrex ETH"),
                            Attribute(key="data_source_id", value="60"),
                            Attribute(
                                key="data_source_hash",
                                value="2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac",
                            ),
                            Attribute(key="external_id", value="7"),
                            Attribute(key="calldata", value="kraken ETH"),
                            Attribute(key="data_source_id", value="60"),
                            Attribute(
                                key="data_source_hash",
                                value="2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac",
                            ),
                            Attribute(key="external_id", value="8"),
                            Attribute(key="calldata", value="bitfinex ETH"),
                            Attribute(key="data_source_id", value="58"),
                            Attribute(
                                key="data_source_hash",
                                value="7e6759fade717a06fb643392bfde837bfc3437da2ded54feed706e6cd35de461",
                            ),
                            Attribute(key="external_id", value="1"),
                            Attribute(key="calldata", value="ETH"),
                        ],
                    ),
                    StringEvent(
                        type="request",
                        attributes=[
                            Attribute(key="id", value="287004"),
                            Attribute(key="client_id", value="Blue"),
                            Attribute(key="oracle_script_id", value="37"),
                            Attribute(key="calldata", value="00000001000000034554480000000000000064"),
                            Attribute(key="ask_count", value="16"),
                            Attribute(key="min_count", value="10"),
                            Attribute(key="gas_used", value="71512"),
                            Attribute(key="validator", value="bandvaloper18tjynh8v0kvf9lmjenx02fgltxk0c6jmm2wcjc"),
                            Attribute(key="validator", value="bandvaloper1w46umthap3cmvqarrznauy25mdhqu45tv8hq62"),
                            Attribute(key="validator", value="bandvaloper1qudzmeu5yr7ryaq9spfpurptvlv4mxehe8x86e"),
                            Attribute(key="validator", value="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa"),
                            Attribute(key="validator", value="bandvaloper1npezmz5cw208gm7l7nhay5xm6h5k4we5axn663"),
                            Attribute(key="validator", value="bandvaloper1d0kcwzukkjl2w2nty3xerqpy3ypdrph67hxx4v"),
                            Attribute(key="validator", value="bandvaloper19j74weeme5ehvmfnduz5swkxysz4twg92swxaf"),
                            Attribute(key="validator", value="bandvaloper1ejnk6k8ny3y5kwr234m3y32p7dxsx2a0wvcpyl"),
                            Attribute(key="validator", value="bandvaloper185sr49ntmfzfc5z52eh0z5m2vjvahwqa6qvk27"),
                            Attribute(key="validator", value="bandvaloper106e65xpz88s5xvnlp5lqx98th9zvpptu7uj7zy"),
                            Attribute(key="validator", value="bandvaloper12dzdxtd2mtnc37nfutwmj0lv8lsfgn6um0e5q5"),
                            Attribute(key="validator", value="bandvaloper1h52l9shahsdzrduwtjt9exc349sehx4s2zydrv"),
                            Attribute(key="validator", value="bandvaloper1u3c40nglllu4upuddlz6l59afq7uuz7lq6z977"),
                            Attribute(key="validator", value="bandvaloper1g4tfgzuxtnfzpnc7drk83n6r6ghkmzwsc7eglq"),
                            Attribute(key="validator", value="bandvaloper1kfj48adjsnrgu83lau6wc646q2uf65rf84tzus"),
                            Attribute(key="validator", value="bandvaloper1t0x8dv4frjnrnl0geegf9l5hrj9wa7qwmjrrwg"),
                        ],
                    ),
                ]
            )
        ],
        gas_wanted=2000000,
        gas_used=789441,
    )
)
