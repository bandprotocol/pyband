import grpc
from google.protobuf import any_pb2
from typing import List

from pyband.proto.oracle.v1 import (
    query_pb2_grpc as oracle_query_grpc,
    query_pb2 as oracle_query,
    oracle_pb2 as oracle_type,
    tx_pb2_grpc as tx_oracle_grpc,
)

from pyband.proto.cosmos.base.tendermint.v1beta1 import (
    query_pb2_grpc as tendermint_query_grpc,
    query_pb2 as tendermint_query,
)

from pyband.proto.cosmos.auth.v1beta1 import (
    query_pb2_grpc as auth_query_grpc,
    query_pb2 as auth_query,
    auth_pb2 as auth_type,
)

from pyband.proto.cosmos.tx.v1beta1 import (
    service_pb2_grpc as tx_service_grpc,
    service_pb2 as tx_service,
    tx_pb2 as tx_type,
)

from pyband.proto.cosmos.base.abci.v1beta1 import abci_pb2 as abci_type

from pyband.exceptions import NotFoundError, NotFoundError, EmptyMsgError


class Client:
    def __init__(self, grpc_endpoint: str):
        channel = grpc.insecure_channel(grpc_endpoint)
        self.stubOracle = oracle_query_grpc.QueryStub(channel)
        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(channel)
        self.stubAuth = auth_query_grpc.QueryStub(channel)
        self.stubTx = tx_service_grpc.ServiceStub(channel)
        self.stubOracleTx = tx_oracle_grpc.MsgStub(channel)

    def get_data_source(self, id: int) -> oracle_type.DataSource:
        return self.stubOracle.DataSource(oracle_query.QueryDataSourceRequest(data_source_id=id)).data_source

    def get_oracle_script(self, id: int) -> oracle_type.OracleScript:
        return self.stubOracle.OracleScript(oracle_query.QueryOracleScriptRequest(oracle_script_id=id)).oracle_script

    def get_request_by_id(self, id: int) -> oracle_query.QueryRequestResponse:
        return self.stubOracle.Request(oracle_query.QueryRequestRequest(request_id=id))

    def get_reporters(self, validator: str) -> oracle_type.ReportersPerValidator.reporters:
        return self.stubOracle.Reporters(oracle_query.QueryReportersRequest(validator_address=validator)).reporter

    def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        return self.stubCosmosTendermint.GetLatestBlock(tendermint_query.GetLatestBlockRequest())

    def get_account(self, address: str) -> auth_type.BaseAccount:
        try:
            account_any = self.stubAuth.Account(auth_query.QueryAccountRequest(address=address)).account
            account = auth_type.BaseAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                return account
        except:
            return None

    # return list of request, if no request, get from report
    def get_request_id_by_tx_hash(self, tx_hash: bytes) -> List[str]:
        tx = self.stubTx.GetTx(tx_service.GetTxRequest(hash=tx_hash))
        request_ids = []
        for tx in tx.tx_response.logs:
            request_event = [event for event in tx.events if event.type == "request" or event.type == "report"]
            if len(request_event) == 1:
                attrs = request_event[0].attributes
                attr_id = [attr for attr in attrs if attr.key == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0].value
                    request_ids.append(request_id)
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids
                     
    def send_tx_sync_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        return self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)
        ).tx_response

    def send_tx_async_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        return self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC)
        ).tx_response

    def send_tx_block_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        return self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK)
        ).tx_response

    def get_chain_id(self) -> str:
        latest_block = self.get_latest_block()
        return latest_block.block.header.chain_id

    def get_reference_data(self, pairs: [str], min_count: int, ask_count: int) -> oracle_query.QueryRequestPriceResponse:
        if (len(pairs) == 0): raise EmptyMsgError("Pairs are required")
        return self.stubOracle.RequestPrice(
        oracle_query.QueryRequestPriceRequest(symbols=pairs, min_count=min_count, ask_count=ask_count))   

    def get_latest_request(self, oid: int, calldata: bytes, min_count: int, ask_count: int) -> oracle_query.QueryRequestSearchResponse:
        return self.stubOracle.RequestSearch(
            oracle_query.QueryRequestSearchRequest(
                oracle_script_id=oid, calldata=calldata, min_count=min_count, ask_count=ask_count
            )
        )

    # ! Haven't implemented yet

    # def get_price_symbols(self, symbols: List[str], min_count: int, ask_count: int) -> oracle_type.PriceResult:
    #     return self.stubOracle.RequestPrice(oracle_query.QueryRequestPriceRequest(symbols=symbols, min_count=min_count, ask_count=ask_count))

    # def get_request_evm_proof_by_request_id(self, request_id: int) -> EVMProof:
