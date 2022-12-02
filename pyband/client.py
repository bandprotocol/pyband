import time
from typing import List

from grpclib.client import Channel

from .data import ReferencePrice, ReferencePriceUpdated
from .exceptions import NotFoundError, EmptyMsgError
from .proto.cosmos.auth.v1beta1 import BaseAccount, QueryAccountRequest
from .proto.cosmos.auth.v1beta1 import QueryStub as AuthQueryStub
from .proto.cosmos.base.abci.v1beta1 import TxResponse
from .proto.cosmos.base.tendermint.v1beta1 import GetLatestBlockRequest, GetLatestBlockResponse
from .proto.cosmos.base.tendermint.v1beta1 import ServiceStub as TendermintServiceStub
from .proto.cosmos.crypto.secp256k1 import PubKey
from .proto.cosmos.tx.v1beta1 import GetTxRequest, BroadcastTxRequest, BroadcastMode, SimulateRequest, SimulateResponse
from .proto.cosmos.tx.v1beta1 import ServiceStub as TxServiceStub
from .proto.oracle.v1 import (
    DataSource,
    OracleScript,
    QueryDataSourceRequest,
    QueryOracleScriptRequest,
    QueryRequestRequest,
    QueryRequestResponse,
    QueryReportersRequest,
    QueryRequestPriceRequest,
    QueryRequestSearchRequest,
    QueryRequestSearchResponse,
)
from .proto.oracle.v1 import MsgStub as OracleMsgStub
from .proto.oracle.v1 import QueryStub as OracleQueryStub


class Client:
    """Class for instantiating a client side connection with BandChain."""

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
        """Closes the connection."""

        self.__channel.close()

    @classmethod
    def from_endpoint(cls, grpc_endpoint: str, port: int, ssl: bool = True):
        """Creates a client instance from a given endpoint and port.

        Args:
            grpc_endpoint: The GRPC endpoint to connect too.
            port: The endpoint port.
            ssl: If true, SSL context is used.

        Returns:
            A Client instance.
        """

        return cls(Channel(host=grpc_endpoint, port=port, ssl=ssl))

    async def get_data_source(self, id: int) -> DataSource:
        """Gets a data source's details.

        Args:
            id: The data source ID.

        Returns:
            The data source details.
        """

        resp = await self.stub_oracle.data_source(QueryDataSourceRequest(data_source_id=id))
        return resp.data_source

    async def get_oracle_script(self, id: int) -> OracleScript:
        """Gets an oracle script's details.

        Args:
            id: The oracle script ID.

        Returns:
            The oracle script details.
        """

        resp = await self.stub_oracle.oracle_script(QueryOracleScriptRequest(oracle_script_id=id))
        return resp.oracle_script

    async def get_request_by_id(self, id: int) -> QueryRequestResponse:
        """Gets a request's details.

        Args:
            id: The request ID.

        Returns:
            The request details.
        """

        resp = await self.stub_oracle.request(QueryRequestRequest(request_id=id))
        return resp

    async def get_reporters(self, validator: str) -> List[str]:
        """Gets a list of reporters associated with a given validator.

        Args:
            validator: The validator's address.

        Returns:
            A list of reporter addresses.
        """

        resp = await self.stub_oracle.reporters(QueryReportersRequest(validator_address=validator))
        return resp.reporter

    async def get_latest_block(self) -> GetLatestBlockResponse:
        """Gets the latest block on chain.

        Returns:
            The details of the latest block.
        """

        return await self.stub_cosmos_tendermint.get_latest_block(GetLatestBlockRequest())

    async def get_account(self, address: str) -> BaseAccount:
        """Gets the account details of a specified address.

        Args:
            address: The address to retrieve the detail of.

        Returns:
            The account details.
        """

        try:
            resp = await self.stub_auth.account(QueryAccountRequest(address=address))
            account = BaseAccount()
            pub_key = PubKey()

            account.parse(resp.account.value)
            account.pub_key = pub_key.parse(account.pub_key.value)
        except Exception as e:
            raise e

        return account

    async def get_request_id_by_tx_hash(self, tx_hash: str) -> List[int]:
        """Gets the request ID of a given transaction hash.

        Args:
            tx_hash: The transaction hash to retrieve the request ID of.

        Returns:
            A list of request IDs.
        """

        tx = await self.stub_tx.get_tx(GetTxRequest(hash=tx_hash))
        request_ids = []
        for log in tx.tx_response.logs:
            request_event = [event for event in log.events if event.type == "request" or event.type == "report"]
            if len(request_event) == 1:
                attrs = request_event[0].attributes
                attr_id = [attr for attr in attrs if attr.key == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0].value
                    request_ids.append(int(request_id))
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids

    async def send_tx_sync_mode(self, tx_bytes: bytes) -> TxResponse:
        """Sends a transaction in sync mode.

        Sends a transaction and waits until the transaction has passed the CheckTx phase.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The transaction response.
        """

        resp = await self.stub_tx.broadcast_tx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=BroadcastMode.BROADCAST_MODE_SYNC)
        )
        return resp.tx_response

    async def send_tx_async_mode(self, tx_bytes: bytes) -> TxResponse:
        """Sends a transaction in async mode.

        Sends a transaction and returns the response immediately, without waiting for the transaction process.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The transaction response.
        """

        resp = await self.stub_tx.broadcast_tx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=BroadcastMode.BROADCAST_MODE_ASYNC)
        )
        return resp.tx_response

    async def send_tx_block_mode(self, tx_bytes: bytes) -> TxResponse:
        """Sends a transaction in block mode.

        Sends a transaction and waits until the transaction has been committed to a block before returning the response.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The transaction response.
        """

        resp = await self.stub_tx.broadcast_tx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=BroadcastMode.BROADCAST_MODE_BLOCK)
        )
        return resp.tx_response

    async def get_chain_id(self) -> str:
        """Gets the chain ID.

        Returns:
            The chain ID.
        """

        latest_block = await self.get_latest_block()
        return latest_block.block.header.chain_id

    async def get_reference_data(self, pairs: List[str], min_count: int, ask_count: int) -> List[ReferencePrice]:
        """Gets the rates of the given cryptocurrency pairs.

        Args:
            pairs: A list of cryptocurrency pairs.
            min_count: The minimum number of validators necessary for the request to proceed to the execution phase.
            ask_count: The number of validators requested to respond to the corresponding request.

        Returns:
            A list of reference prices, which contains the pair, its rate and its last updated time.
        """

        if len(pairs) == 0:
            raise EmptyMsgError("Pairs are required")

        symbols = set([symbol for pair in pairs for symbol in pair.split("/") if symbol != "USD"])

        price_data = await self.stub_oracle.request_price(
            QueryRequestPriceRequest(
                symbols=list(symbols),
                min_count=min_count,
                ask_count=ask_count,
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

    async def get_latest_request(
        self, oid: int, calldata: str, min_count: int, ask_count: int
    ) -> QueryRequestSearchResponse:
        """Gets the latest on chain request.

        Args:
            oid: The oracle script ID.
            calldata: The calldata of the request.
            min_count: The minimum number of validators necessary for the request to proceed to the execution phase.
            ask_count: The number of validators requested to respond to the corresponding request.

        Returns:
            The request details.
        """
        return await self.stub_oracle.request_search(
            QueryRequestSearchRequest(
                oracle_script_id=oid, calldata=calldata, ask_count=ask_count, min_count=min_count
            )
        )

    async def get_tx_response(self, tx_hash: str) -> TxResponse:
        """Gets the tx response from a tx hash.

        Args:
            tx_hash: The transaction hash to retrieve the tx response of.

        Returns:
            The tx response.
        """
        resp = await self.stub_tx.get_tx(GetTxRequest(hash=tx_hash))
        return resp.tx_response

    async def simulate_tx(self, tx_bytes: bytes) -> SimulateResponse:
        """Simulates a transaction from the tx_bytes.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The simulated response.
        """
        return await self.stub_tx.simulate(SimulateRequest(tx_bytes=tx_bytes))
