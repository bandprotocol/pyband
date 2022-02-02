import pytest
import grpc

from pyband.wallet import PrivateKey
from pyband.transaction import Transaction

# Servicers
from pyband.proto.oracle.v1.query_pb2_grpc import QueryServicer as OracleServicerBase
from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import ServiceServicer as CosmosTxServicerBase


# Types
from pyband.proto.oracle.v1.oracle_pb2 import OracleScript
from pyband.proto.oracle.v1.tx_pb2 import MsgCreateOracleScript, MsgEditOracleScript

from pyband.proto.cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest, BroadcastTxResponse
from pyband.proto.cosmos.base.abci.v1beta1.abci_pb2 import TxResponse

MNEMONIC = "s"
PRIVATE_KEY = PrivateKey.from_mnemonic(MNEMONIC)
PUBLIC_KEY = PRIVATE_KEY.to_public_key()
ADDRESS = PUBLIC_KEY.to_address()
SENDER = ADDRESS.to_acc_bech32()

success_os_file = open('tests/mock_files/sample_os.wasm', 'rb')
success_os_bytes = success_os_file.read()
success_os_file.close()


empty_os_file = open('tests/mock_files/empty_os.wasm', 'rb')
empty_os_bytes = empty_os_file.read()
empty_os_file.close()

request_msg_create_os_success = MsgCreateOracleScript(
    name="Standard Dataset Crypto",
    description="Standard Dataset Crypto Description",
    sender=SENDER,
    owner=SENDER,
    schema="{symbols:[string],multiplier:u64}/{rates:[u64]}",
    source_code_url="https://mockurl.com",
    code=success_os_bytes
)

request_msg_create_os_empty_code = MsgCreateOracleScript(
    name="Cryptocurrency Price in USD",
    description="Oracle script that queries the average cryptocurrency price using current price data from CoinGecko, CryptoCompare, and Binance",
    sender=SENDER,
    owner="band1m5lq9u533qaya4q3nfyl6ulzqkpkhge9q8tpzs",
    schema="{symbol:string,multiplier:u64}/{px:u64}",
    source_code_url="https://ipfs.io/ipfs/QmQqxHLszpbCy8Hk2ame3pPAxUUAyStBrVdGdDgrfAngAv",
    code=empty_os_bytes
)

request_msg_edit_os_success = MsgEditOracleScript(
    oracle_script_id=122,
    name="Standard Dataset Crypto",
    description="Standard Dataset Crypto Description",
    sender=SENDER,
    owner=SENDER,
    schema="{symbols:[string],multiplier:u64}/{rates:[u64]}",
    source_code_url="https://mockurl.com",
    code=success_os_bytes
)

request_msg_edit_os_empty_code = MsgEditOracleScript(
    oracle_script_id=122,
    name="Cryptocurrency Price in USD",
    description="Oracle script that queries the average cryptocurrency price using current price data from CoinGecko, CryptoCompare, and Binance",
    sender=SENDER,
    owner="band1m5lq9u533qaya4q3nfyl6ulzqkpkhge9q8tpzs",
    schema="{symbol:string,multiplier:u64}/{px:u64}",
    source_code_url="https://ipfs.io/ipfs/QmQqxHLszpbCy8Hk2ame3pPAxUUAyStBrVdGdDgrfAngAv",
    code=empty_os_bytes
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
        if request.tx_bytes == getTxBytes(request_msg_create_os_success):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3403558,
                    txhash="32C8A5C678D7296E418071199A3DEA52318A241ED6EE880BF91C474C1F17BB35",
                    data="0A220A202F6F7261636C652E76312E4D73674372656174654F7261636C65536372697074",
                )
            )
        elif request.tx_bytes == getTxBytes(request_msg_create_os_empty_code):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="BA1E6D8B6B3E07DF18FF0058D0066249A8260D60BE8F02F08BD5D01AA0A109E3",
                    raw_log="empty wasm code",
                )
            )
        elif request.tx_bytes == getTxBytes(request_msg_edit_os_success):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    height=3406776,
                    txhash="5D0C6DEA932D7684284F7EABB4F97A79C56CBFF00972FFA30399821CFDBDE158",
                    data="0A200A1E2F6F7261636C652E76312E4D7367456469744F7261636C65536372697074",
                )
            )
        elif request.tx_bytes == getTxBytes(request_msg_edit_os_empty_code):
            return BroadcastTxResponse(
                tx_response=TxResponse(
                    txhash="5E00BCF8DA524DEBC60800C4EAA4FA1618C7D69B2703B821FD4141D53AD8FBBA",
                    code=21,
                    raw_log="empty wasm code",
                )
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


def test_create_oracle_script_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_create_os_success))

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3403558,
            txhash="32C8A5C678D7296E418071199A3DEA52318A241ED6EE880BF91C474C1F17BB35",
            data="0A220A202F6F7261636C652E76312E4D73674372656174654F7261636C65536372697074",
        )
    )

    assert tx_response == mock_result.tx_response


def test_create_oracle_script_empty_code(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_create_os_empty_code))

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="BA1E6D8B6B3E07DF18FF0058D0066249A8260D60BE8F02F08BD5D01AA0A109E3",
            raw_log="empty wasm code",
        )
    )

    assert tx_response == mock_result.tx_response


def test_edit_oracle_script_success(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_edit_os_success))

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            height=3406776,
            txhash="5D0C6DEA932D7684284F7EABB4F97A79C56CBFF00972FFA30399821CFDBDE158",
            data="0A200A1E2F6F7261636C652E76312E4D7367456469744F7261636C65536372697074",
        )
    )

    assert tx_response == mock_result.tx_response


def test_edit_oracle_script_invalid_id(pyband_client):
    with pytest.raises(TypeError):
        pyband_client.get_oracle_script("hi")


def test_edit_oracle_script_empty_code(pyband_client):
    tx_response = pyband_client.send_tx_block_mode(
        getTxBytes(request_msg_edit_os_empty_code))

    mock_result = BroadcastTxResponse(
        tx_response=TxResponse(
            txhash="5E00BCF8DA524DEBC60800C4EAA4FA1618C7D69B2703B821FD4141D53AD8FBBA",
            code=21,
            raw_log="empty wasm code",
        )
    )

    assert tx_response == mock_result.tx_response
