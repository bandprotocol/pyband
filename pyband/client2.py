from pyband.google.protobuf import any_pb2 
import grpc
from pyband.oracle.v1 import query_pb2_grpc as oracle_query_grpc
from pyband.oracle.v1 import query_pb2 as oracle_query
from pyband.oracle.v1 import oracle_pb2 as oracle_type

from pyband.cosmos.base.tendermint.v1beta1 import query_pb2_grpc as tendermint_query_grpc
from pyband.cosmos.base.tendermint.v1beta1 import query_pb2 as tendermint_query

from pyband.cosmos.auth.v1beta1 import query_pb2_grpc as auth_query_grpc
from pyband.cosmos.auth.v1beta1 import query_pb2 as auth_query
from pyband.cosmos.auth.v1beta1 import auth_pb2 as auth_type


from pyband.cosmos.base.reflection.v2alpha1 import reflection_pb2_grpc as base_reflection_grpc
from pyband.cosmos.base.reflection.v2alpha1 import reflection_pb2 as base_reflection

from pyband.cosmos.tx.v1beta1 import service_pb2_grpc as tx_service_grpc
from pyband.cosmos.tx.v1beta1 import service_pb2 as tx_service
from pyband.cosmos.tx.v1beta1 import tx_pb2 as tx_type

from pyband.oracle.v1 import tx_pb2_grpc as tx_oracle_grpc
from pyband.oracle.v1 import tx_pb2 as tx_oracle

from typing import List, Optional
from pyband.wallet import PrivateKey, Address
from pyband.message import MsgRequest
from pyband.obi import PyObi
from pyband.transaction import Transaction



class Cli:
    def __init__(self, grc_endpoint: str):
        channel = grpc.insecure_channel(grc_endpoint)
        self.stubOracle = oracle_query_grpc.QueryStub(channel)
        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(channel)
        self.stubAuth = auth_query_grpc.QueryStub(channel)
        self.stubCosmosBase = base_reflection_grpc.ReflectionServiceStub(
            channel)
        self.stubTx = tx_service_grpc.ServiceStub(channel)
        self.stubOracleTx = tx_oracle_grpc.MsgStub(channel)

    def create_transaction(self):
        CHAIN_ID = "band-laozi-testnet1" # Should use get_chain_id
        MNEMONIC = "foo"
        PK = PrivateKey.from_mnemonic(MNEMONIC)
        sender_addr = PK.to_pubkey().to_address()
        sender = sender_addr.to_acc_bech32()
        obi = PyObi("{symbols:[string],multiplier:u64}/{rates:[u64]}")
        calldata = obi.encode({"symbols": ["ETH","BTC","BAND","MIR","UNI"], "multiplier": 100})
        oid = 3
        ask_count = 16
        min_count = 10
        client = "Bubu"
        msg = tx_oracle.MsgRequestData(
            oracle_script_id=oid,
            calldata=calldata,
            ask_count=ask_count,
            min_count=min_count,
            client_id=client,
            fee_limit=[],
            prepare_gas=20000,
            execute_gas=20000,
            sender=sender,
        )
        account = self.get_account(sender)
        account_num = account.account_number
        sequence = account.sequence
        
        msg_any = any_pb2.Any()
        msg_any.Pack(msg)
        
        # ! Getting error here! messages and msg_any are not in the same type
        body = tx_type.TxBody(
            messages=[any_pb2.Any().Pack(msg)],
            memo='',
        )
        

    def get_data_source(self, id: int) -> oracle_type.DataSource:
        print(oracle_type.DataSource)
        return self.stubOracle.DataSource(oracle_query.QueryDataSourceRequest(data_source_id=id)).data_source

    def get_oracle_script(self, id: int) -> oracle_type.OracleScript:
        print(oracle_type.OracleScript)
        return self.stubOracle.OracleScript(oracle_query.QueryOracleScriptRequest(oracle_script_id=id)).oracle_script

    def get_request_by_id(self, id: int):
        return self.stubOracle.Request(oracle_query.QueryRequestRequest(request_id=id))

    def get_reporters(self, validator: str) -> oracle_type.ReportersPerValidator.reporters:
        return self.stubOracle.Reporters(oracle_query.QueryReportersRequest(validator_address=validator)).reporter

    def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        return self.stubCosmosTendermint.GetLatestBlock(tendermint_query.GetLatestBlockRequest())

    def get_account(self, address: str) -> any:
        account_any = self.stubAuth.Account(auth_query.QueryAccountRequest(address=address)).account
        account = auth_type.BaseAccount()
        account_any.Unpack(account)
        return account

    def get_request_id_by_tx_hash(self, tx_hash: bytes) -> str:
        tx = self.stubTx.GetTx(tx_service.GetTxRequest(
            hash=tx_hash)).tx_response.logs[0]
        return tx.events[2].attributes[0].value
   
    def send_tx_sync_mode(self, tx_byte: bytes) -> tx_type.TxRaw: 
        return self.stubTx.BroadcastTx(tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)).tx_response

    def send_tx_async_mode(self, tx_byte: bytes) -> tx_type.TxRaw:
        return self.stubTx.BroadcastTx(tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC))

    def send_tx_block_mode(self, tx_byte: bytes) -> tx_type.TxRaw:
        return self.stubTx.BroadcastTx(tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK))

    # ! ANCHOR Not working - Path is not working yet
    # def get_chain_id(self) -> str:
    #     print(self.stubCosmosBase.GetChainDescriptor(
    #         base_reflection.GetChainDescriptorRequest()))
  
    # def get_reference_data(self, pairs: List[str], min_count: int, ask_count: int) -> List[ReferencePrice]:
    #     symbols = set(
    #         [symbol for pair in pairs for symbol in pair.split("/") if symbol != "USD"])
    #     return self.stubOracle.RequestPrice(oracle_query.QueryRequestPriceRequest(symbols=symbols, min_count=min_count, ask_count=ask_count))

    # def get_price_symbols(self, symbols: List[str], min_count: int, ask_count: int) -> oracle_type.PriceResult:
    #     return self.stubOracle.RequestPrice(oracle_query.QueryRequestPriceRequest(symbols=symbols, min_count=min_count, ask_count=ask_count))

    # def get_latest_request(self, oid: int, calldata: bytes, min_count: int, ask_count: int) -> oracle_type.Result:
    #     return self.stubOracle.RequestSearch(oracle_query.QueryRequestSearchRequest(oracle_script_id=oid, calldata=calldata, min_count=min_count, ask_count=ask_count))

    # ANCHOR Haven't implemented yet
    # def get_request_evm_proof_by_request_id(self, request_id: int) -> EVMProof:
