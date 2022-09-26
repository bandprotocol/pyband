import asyncio
import time
from typing import List, Optional, Any

from grpclib.client import Channel
from grpclib.exceptions import GRPCError

from .data import ReferencePrice, ReferencePriceUpdated
from .exceptions import NotFoundError, EmptyMsgError
from .proto.cosmos.auth.v1beta1 import BaseAccount, QueryAccountRequest, QueryAccountResponse
from .proto.cosmos.auth.v1beta1 import QueryStub as AuthQueryStub
from .proto.cosmos.base.abci.v1beta1 import TxResponse
from .proto.cosmos.base.tendermint.v1beta1 import GetLatestBlockRequest, GetLatestBlockResponse
from .proto.cosmos.base.tendermint.v1beta1 import ServiceStub as TendermintServiceStub
from .proto.cosmos.crypto.secp256k1 import PubKey
from .proto.cosmos.tx.v1beta1 import GetTxRequest, BroadcastTxRequest, BroadcastTxResponse, BroadcastMode
from .proto.cosmos.tx.v1beta1 import ServiceStub as TxServiceStub
from .proto.oracle.v1 import (
    DataSource,
    OracleScript,
    QueryDataSourceRequest,
    QueryDataSourceResponse,
    QueryOracleScriptRequest,
    QueryOracleScriptResponse,
    QueryRequestRequest,
    QueryRequestResponse,
    QueryReportersRequest,
    QueryReportersResponse,
    QueryRequestPriceRequest,
    QueryRequestPriceResponse,
    QueryRequestSearchRequest,
    QueryRequestSearchResponse,
)
from .proto.oracle.v1 import MsgStub as OracleMsgStub
from .proto.oracle.v1 import QueryStub as OracleQueryStub


class Client:
    def __init__(self, channel: Channel):
        self.__channel = channel
        self.stub_oracle = OracleQueryStub(self.__channel)
        self.stub_cosmos_tendermint = TendermintServiceStub(self.__channel)
        self.stub_auth = AuthQueryStub(self.__channel)
        self.stub_tx = TxServiceStub(self.__channel)
        self.stub_oracle_tx = OracleMsgStub(self.__channel)

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        self.__channel.close()

    @classmethod
    def from_endpoint(cls, grpc_endpoint: str, port: int, insecure: bool = False):
        return cls(
            Channel(
                host=grpc_endpoint,
                port=port,
                ssl=False if insecure else True,
            )
        )

    @staticmethod
    def __run_async(coroutine) -> Any:
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(coroutine)
        return result

    def get_data_source(self, id: int) -> DataSource:
        resp: QueryDataSourceResponse = self.__run_async(
            self.stub_oracle.data_source(QueryDataSourceRequest(data_source_id=id))
        )
        return resp.data_source

    def get_oracle_script(self, id: int) -> OracleScript:
        resp: QueryOracleScriptResponse = self.__run_async(
            self.stub_oracle.oracle_script(QueryOracleScriptRequest(oracle_script_id=id))
        )
        return resp.oracle_script

    def get_request_by_id(self, id: int) -> QueryRequestResponse:
        resp: QueryRequestResponse = self.__run_async(self.stub_oracle.request(QueryRequestRequest(request_id=id)))
        return resp

    def get_reporters(self, validator: str) -> QueryReportersResponse.reporter:
        resp: QueryReportersResponse = self.__run_async(
            self.stub_oracle.reporters(QueryReportersRequest(validator_address=validator))
        )
        return resp.reporter

    def get_latest_block(self) -> GetLatestBlockResponse:
        resp: GetLatestBlockResponse = self.__run_async(
            self.stub_cosmos_tendermint.get_latest_block(GetLatestBlockRequest())
        )
        return resp

    def get_account(self, address: str) -> Optional[BaseAccount]:
        try:
            resp: QueryAccountResponse = self.__run_async(self.stub_auth.account(QueryAccountRequest(address=address)))
            account = BaseAccount()
            pub_key = PubKey()

            account.parse(resp.account.value)
            account.pub_key = pub_key.parse(account.pub_key.value)

            return account
        except Exception:
            return None

    def get_request_id_by_tx_hash(self, tx_hash: str) -> List[int]:
        tx: GetTxRequest = self.__run_async(self.stub_tx.get_tx(GetTxRequest(hash=tx_hash)))
        request_ids = []
        for tx in tx.tx_response.logs:
            request_event = [event for event in tx.events if event.type == "request" or event.type == "report"]
            if len(request_event) == 1:
                attrs = request_event[0].attributes
                attr_id = [attr for attr in attrs if attr.key == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0].value
                    request_ids.append(int(request_id))
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids

    def send_tx_sync_mode(self, tx_byte: bytes) -> TxResponse:
        resp: BroadcastTxResponse = self.__run_async(
            self.stub_tx.broadcast_tx(BroadcastTxRequest(tx_bytes=tx_byte, mode=BroadcastMode.BROADCAST_MODE_SYNC))
        )
        return resp.tx_response

    def send_tx_async_mode(self, tx_byte: bytes) -> TxResponse:
        resp: BroadcastTxResponse = self.__run_async(
            self.stub_tx.broadcast_tx(BroadcastTxRequest(tx_bytes=tx_byte, mode=BroadcastMode.BROADCAST_MODE_ASYNC))
        )
        return resp.tx_response

    def send_tx_block_mode(self, tx_byte: bytes) -> TxResponse:
        resp: BroadcastTxResponse = self.__run_async(
            self.stub_tx.broadcast_tx(BroadcastTxRequest(tx_bytes=tx_byte, mode=BroadcastMode.BROADCAST_MODE_BLOCK))
        )
        return resp.tx_response

    def get_chain_id(self) -> str:
        latest_block = self.get_latest_block()
        return latest_block.block.header.chain_id

    def get_reference_data(self, pairs: List[str], min_count: int, ask_count: int) -> List[ReferencePrice]:
        if len(pairs) == 0:
            raise EmptyMsgError("Pairs are required")

        symbols = set([symbol for pair in pairs for symbol in pair.split("/") if symbol != "USD"])

        price_data: QueryRequestPriceResponse = self.__run_async(
            self.stub_oracle.request_price(
                QueryRequestPriceRequest(symbols=list(symbols), min_count=min_count, ask_count=ask_count)
            )
        )

        symbol_dict = {
            "USD": {
                "multiplier": 1000000000,
                "px": 1000000000,
                "resolve_time": int(time.time()),
            }
        }

        for price in price_data.price_results:
            symbol_dict[price.symbol] = {
                "multiplier": price.multiplier,
                "px": price.px,
                "resolve_time": price.resolve_time,
            }

        results = []
        for pair in pairs:
            base_symbol, quote_symbol = pair.split("/")

            quote_rate = int(symbol_dict[base_symbol]["px"]) / int(symbol_dict[base_symbol]["multiplier"])
            base_rate = int(symbol_dict[quote_symbol]["px"]) / int(symbol_dict[quote_symbol]["multiplier"])
            rate = quote_rate / base_rate

            rate_updated_at = ReferencePriceUpdated(
                int(symbol_dict[base_symbol]["resolve_time"]),
                int(symbol_dict[quote_symbol]["resolve_time"]),
            )

            results.append(ReferencePrice(pair, rate=rate, updated_at=rate_updated_at))

        return results

    def get_latest_request(
        self, oid: int, calldata: str, min_count: int, ask_count: int
    ) -> QueryRequestSearchResponse:
        resp: QueryRequestSearchResponse = self.__run_async(
            self.stub_oracle.request_search(
                QueryRequestSearchRequest(
                    oracle_script_id=oid, calldata=calldata, ask_count=ask_count, min_count=min_count
                )
            )
        )
        return resp
