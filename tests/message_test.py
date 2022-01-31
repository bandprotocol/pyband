import pytest

from pyband.wallet import PrivateKey
from pyband.transaction import Transaction

from pyband.proto.cosmos.staking.v1beta1.tx_pb2 import MsgDelegate, MsgBeginRedelegate, MsgUndelegate
from pyband.proto.cosmos.distribution.v1beta1.tx_pb2 import MsgWithdrawDelegatorReward
from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin

from pyband.proto.cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest, BroadcastTxResponse
from pyband.proto.cosmos.base.abci.v1beta1.abci_pb2 import TxResponse

from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import ServiceServicer as CosmosTxServicerBase

from pyband.exceptions import NotFoundError, EmptyMsgError

MNEMONIC = "s"
PRIVATE_KEY = PrivateKey.from_mnemonic(MNEMONIC)
PUBLIC_KEY = PRIVATE_KEY.to_public_key()
ADDRESS = PUBLIC_KEY.to_address()
SENDER = ADDRESS.to_acc_bech32()

request_msg_delegate = MsgDelegate(
    delegator_address=SENDER,
    validator_address="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa",
    amount=Coin(amount="1000", denom="uband")
)

request_msg_delegate_invalid_coin = MsgDelegate(
    delegator_address=SENDER,
    validator_address="124",
    amount=Coin(amount="-1000", denom="uband")
)

request_msg_redelegate = MsgBeginRedelegate(
    delegator_address=SENDER,
    validator_src_address="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa",
    validator_dst_address="bandvaloper1zkf9qzs7ayf3uqksxqwve8q693dsdhxk800wvw",
    amount=Coin(amount="1000", denom="uband")
)

request_msg_redelegate_invalid_coin = MsgBeginRedelegate(
    delegator_address=SENDER,
    validator_src_address="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa",
    validator_dst_address="bandvaloper1zkf9qzs7ayf3uqksxqwve8q693dsdhxk800wvw",
    amount=Coin(amount="-1000", denom="uband")
)

request_msg_undelegate = MsgUndelegate(
    delegator_address=SENDER,
    validator_address="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa",
    amount=Coin(amount="100", denom="uband")
)

request_msg_undelegate_invalid_coin = MsgUndelegate(
    delegator_address=SENDER,
    validator_address="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa",
    amount=Coin(amount="-100", denom="uband")
)

request_msg_withdraw_reward = MsgWithdrawDelegatorReward(
    delegator_address=SENDER,
    validator_address="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa"
)

request_msg_withdraw_reward_invalid_address = MsgWithdrawDelegatorReward(
    delegator_address='',
    validator_address="bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa",
)


@pytest.fixture(scope="module")
def pyband_client(_grpc_server, grpc_addr):
    from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import add_ServiceServicer_to_server as add_cosmos_tx

    add_cosmos_tx(CosmosTransactionServicer(), _grpc_server)

    _grpc_server.add_insecure_port(grpc_addr)
    _grpc_server.start()

    from pyband.client import Client

    yield Client(grpc_addr, insecure=True)
    _grpc_server.stop(grace=None)


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
        if request.tx_bytes == getTxBytes(request_msg_delegate):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3358347,
                    txhash="C995E379BC5DEC8CF697568FDBB2DB8D661EEE12AA3F4AB95F52E6B69D29ED92",
                    data="0A250A232F636F736D6F732E7374616B696E672E763162657461312E4D736744656C6567617465",
                )
            )

        elif request.tx_bytes == getTxBytes(request_msg_delegate_invalid_coin):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    code=18,
                    txhash="89BE7815FD472D50413D3084E3DD6186500F22BB8ABEAAE508D4058D1617E33C",
                    raw_log="invalid delegation amount: invalid request"
                )
            )

        elif request.tx_bytes == getTxBytes(request_msg_redelegate):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3358678,
                    txhash="B9FE6BF7274DF34DA015408AE2861AD06D7870BED407405AA67B1F4E644DC511",
                    data="0A3C0A2A2F636F736D6F732E7374616B696E672E763162657461312E4D7367426567696E526564656C6567617465120E0A0C08C3D2CD900610DEB1EFA203",
                )
            )

        elif request.tx_bytes == getTxBytes(request_msg_redelegate_invalid_coin):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    code=18,
                    txhash="DA4F78DEF7440300AB364EE3A9759158D087FE57671A67B290E55F450892392F",
                    raw_log="invalid shares amount: invalid request"
                )
            )

        elif request.tx_bytes == getTxBytes(request_msg_undelegate):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3359095,
                    txhash="F7726773EBBE103A5DD4A2B0AEB4D1E4160EB75811CA541B9AEF81242C5B4EB4",
                    data="0A370A252F636F736D6F732E7374616B696E672E763162657461312E4D7367556E64656C6567617465120E0A0C08F9DECD900610EC969AC202",
                )
            )

        elif request.tx_bytes == getTxBytes(request_msg_undelegate_invalid_coin):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    code=18,
                    txhash="657C82B7C5647D45DE2D9BB9D35CEE145E5CC888EC6E9D50910315EF420E7104",
                    raw_log="invalid shares amount: invalid request"
                )
            )

        elif request.tx_bytes == getTxBytes(request_msg_withdraw_reward):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3359924,
                    txhash="977710697F6BA545853A02D77915FBDCE47DF8439362193A27874DDD3BD16A40",
                    data="0A390A372F636F736D6F732E646973747269627574696F6E2E763162657461312E4D7367576974686472617744656C656761746F72526577617264",
                )
            )

        elif request.tx_bytes == getTxBytes(request_msg_withdraw_reward_invalid_address):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3359924,
                    txhash="977710697F6BA545853A02D77915FBDCE47DF8439362193A27874DDD3BD16A40",
                    data="0A390A372F636F736D6F732E646973747269627574696F6E2E763162657461312E4D7367576974686472617744656C656761746F72526577617264",
                )
            )


def test_message_delegate_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_delegate))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3358347,
            txhash="C995E379BC5DEC8CF697568FDBB2DB8D661EEE12AA3F4AB95F52E6B69D29ED92",
            data="0A250A232F636F736D6F732E7374616B696E672E763162657461312E4D736744656C6567617465",
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_delegate_invalid_coin(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_delegate_invalid_coin))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            code=18,
            txhash="89BE7815FD472D50413D3084E3DD6186500F22BB8ABEAAE508D4058D1617E33C",
            raw_log="invalid delegation amount: invalid request"
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_redelegate_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_redelegate))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3358678,
            txhash="B9FE6BF7274DF34DA015408AE2861AD06D7870BED407405AA67B1F4E644DC511",
            data="0A3C0A2A2F636F736D6F732E7374616B696E672E763162657461312E4D7367426567696E526564656C6567617465120E0A0C08C3D2CD900610DEB1EFA203",
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_redelegate_invalid_coin(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_redelegate_invalid_coin))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            code=18,
            txhash="DA4F78DEF7440300AB364EE3A9759158D087FE57671A67B290E55F450892392F",
            raw_log="invalid shares amount: invalid request"
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_undelegate_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_undelegate))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3359095,
            txhash="F7726773EBBE103A5DD4A2B0AEB4D1E4160EB75811CA541B9AEF81242C5B4EB4",
            data="0A370A252F636F736D6F732E7374616B696E672E763162657461312E4D7367556E64656C6567617465120E0A0C08F9DECD900610EC969AC202",
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_undelegate_invalid_coin(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_undelegate_invalid_coin))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            code=18,
            txhash="657C82B7C5647D45DE2D9BB9D35CEE145E5CC888EC6E9D50910315EF420E7104",
            raw_log="invalid shares amount: invalid request"
        )
    )

    assert tx_response == mock_result.tx_response


def test_message_withdraw_reward_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_withdraw_reward))
    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3359924,
            txhash="977710697F6BA545853A02D77915FBDCE47DF8439362193A27874DDD3BD16A40",
            data="0A390A372F636F736D6F732E646973747269627574696F6E2E763162657461312E4D7367576974686472617744656C656761746F72526577617264",
        )
    )

    assert tx_response == mock_result.tx_response
