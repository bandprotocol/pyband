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

from pyband.cosmos.tx.signing.v1beta1 import signing_pb2 as tx_sign

from typing import List, Optional
from pyband.wallet import PrivateKey
from pyband.obi import PyObi

from google.protobuf import any_pb2


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

    # def create_transaction(self):
    #     # Create mock up data
    #     CHAIN_ID = "band-laozi-testnet1"  # Should use get_chain_id
    #     MNEMONIC = "foo"
    #     PK = PrivateKey.from_mnemonic(MNEMONIC)
    #     public_key = PK.to_pubkey()
    #     sender_addr = public_key.to_address()
    #     sender = sender_addr.to_acc_bech32()
    #     obi = PyObi("{symbols:[string],multiplier:u64}/{rates:[u64]}")
    #     calldata = obi.encode(
    #         {"symbols": ["ETH", "BTC", "BAND", "MIR", "UNI"], "multiplier": 100})
    #     oid = 3
    #     ask_count = 16
    #     min_count = 10
    #     client = "Bubu"
    #     msg = tx_oracle.MsgRequestData(
    #         oracle_script_id=oid,
    #         calldata=calldata,
    #         ask_count=ask_count,
    #         min_count=min_count,
    #         client_id=client,
    #         fee_limit=[],
    #         prepare_gas=20000,
    #         execute_gas=20000,
    #         sender=sender,
    #     )
    #     account = self.get_account(sender)
    #     account_num = account.account_number
    #     sequence = account.sequence
    #     msg_any = any_pb2.Any()
    #     msg_any.Pack(msg, type_url_prefix="")

    #     body = tx_type.TxBody(
    #         messages=[msg_any],
    #         memo='',
    #     )
    #     mode_info = tx_type.ModeInfo(
    #         single=tx_type.ModeInfo.Single(mode=tx_sign.SIGN_MODE_DIRECT))

    #     signer_info = tx_type.SignerInfo(
    #         mode_info=mode_info, sequence=sequence)
        
    #     # # Calculate estimated gas
    #     # tx = tx_type.Tx(body=body, auth_info=)
    #     # self.stubTx.Simulate(tx_service.SimulateRequest(tx))
        
    #     fee = tx_type.Fee(amount=[], gas_limit=200000)
    #     auth_info = tx_type.AuthInfo(signer_infos=[signer_info], fee=fee)

    #     body_bytes = body.SerializeToString()
    #     auth_info_bytes = auth_info.SerializeToString()
    #     sign_doc = tx_type.SignDoc(
    #         body_bytes=body_bytes, auth_info_bytes=auth_info_bytes, chain_id=CHAIN_ID, account_number=account_num)

    #     signature = PK.sign(sign_doc.SerializeToString())
    #     tx_raw = tx_type.TxRaw(
    #         body_bytes=body_bytes, auth_info_bytes=auth_info_bytes, signatures=[signature])
    #     tx_raw_bytes = tx_raw.SerializeToString()

    #     # print(self.send_tx_async_mode(tx_raw_bytes))

    def get_data_source(self, id: int) -> oracle_type.DataSource:
        return self.stubOracle.DataSource(oracle_query.QueryDataSourceRequest(data_source_id=id)).data_source

    def get_oracle_script(self, id: int) -> oracle_type.OracleScript:
        return self.stubOracle.OracleScript(oracle_query.QueryOracleScriptRequest(oracle_script_id=id)).oracle_script

    def get_request_by_id(self, id: int):
        return self.stubOracle.Request(oracle_query.QueryRequestRequest(request_id=id))

    def get_reporters(self, validator: str) -> oracle_type.ReportersPerValidator.reporters:
        return self.stubOracle.Reporters(oracle_query.QueryReportersRequest(validator_address=validator)).reporter

    def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        return self.stubCosmosTendermint.GetLatestBlock(tendermint_query.GetLatestBlockRequest())

    def get_account(self, address: str) -> any:
        account_any = self.stubAuth.Account(
            auth_query.QueryAccountRequest(address=address)).account
        account = auth_type.BaseAccount()
        if account_any.Is(account.DESCRIPTOR):
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
