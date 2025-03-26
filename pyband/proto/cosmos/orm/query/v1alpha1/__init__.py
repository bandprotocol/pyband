# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/orm/query/v1alpha1/query.proto
# plugin: python-betterproto
# This file has been @generated
import builtins
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ....base.query import v1beta1 as __base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class GetRequest(betterproto.Message):
    """GetRequest is the Query/Get request type."""

    message_name: str = betterproto.string_field(1)
    """
    message_name is the fully-qualified message name of the ORM table being queried.
    """

    index: str = betterproto.string_field(2)
    """
    index is the index fields expression used in orm definitions. If it
     is empty, the table's primary key is assumed. If it is non-empty, it must
     refer to an unique index.
    """

    values: List["IndexValue"] = betterproto.message_field(3)
    """
    values are the values of the fields corresponding to the requested index.
     There must be as many values provided as there are fields in the index and
     these values must correspond to the index field types.
    """


@dataclass(eq=False, repr=False)
class GetResponse(betterproto.Message):
    """GetResponse is the Query/Get response type."""

    result: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    """
    result is the result of the get query. If no value is found, the gRPC
     status code NOT_FOUND will be returned.
    """


@dataclass(eq=False, repr=False)
class ListRequest(betterproto.Message):
    """ListRequest is the Query/List request type."""

    message_name: str = betterproto.string_field(1)
    """
    message_name is the fully-qualified message name of the ORM table being queried.
    """

    index: str = betterproto.string_field(2)
    """
    index is the index fields expression used in orm definitions. If it
     is empty, the table's primary key is assumed.
    """

    prefix: "ListRequestPrefix" = betterproto.message_field(3, group="query")
    """prefix defines a prefix query."""

    range: "ListRequestRange" = betterproto.message_field(4, group="query")
    """range defines a range query."""

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(5)
    """pagination is the pagination request."""


@dataclass(eq=False, repr=False)
class ListRequestPrefix(betterproto.Message):
    """Prefix specifies the arguments to a prefix query."""

    values: List["IndexValue"] = betterproto.message_field(1)
    """
    values specifies the index values for the prefix query.
     It is valid to special a partial prefix with fewer values than
     the number of fields in the index.
    """


@dataclass(eq=False, repr=False)
class ListRequestRange(betterproto.Message):
    """Range specifies the arguments to a range query."""

    start: List["IndexValue"] = betterproto.message_field(1)
    """
    start specifies the starting index values for the range query.
     It is valid to provide fewer values than the number of fields in the
     index.
    """

    end: List["IndexValue"] = betterproto.message_field(2)
    """
    end specifies the inclusive ending index values for the range query.
     It is valid to provide fewer values than the number of fields in the
     index.
    """


@dataclass(eq=False, repr=False)
class ListResponse(betterproto.Message):
    """ListResponse is the Query/List response type."""

    results: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    """results are the results of the query."""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(5)
    """pagination is the pagination response."""


@dataclass(eq=False, repr=False)
class IndexValue(betterproto.Message):
    """
    IndexValue represents the value of a field in an ORM index expression.
    """

    uint: int = betterproto.uint64_field(1, group="value")
    """
    uint specifies a value for an uint32, fixed32, uint64, or fixed64
     index field.
    """

    int: builtins.int = betterproto.int64_field(2, group="value")
    """
    int64 specifies a value for an int32, sfixed32, int64, or sfixed64
     index field.
    """

    str: builtins.str = betterproto.string_field(3, group="value")
    """str specifies a value for a string index field."""

    bytes: builtins.bytes = betterproto.bytes_field(4, group="value")
    """bytes specifies a value for a bytes index field."""

    enum: builtins.str = betterproto.string_field(5, group="value")
    """enum specifies a value for an enum index field."""

    bool: builtins.bool = betterproto.bool_field(6, group="value")
    """bool specifies a value for a bool index field."""

    timestamp: datetime = betterproto.message_field(7, group="value")
    """timestamp specifies a value for a timestamp index field."""

    duration: timedelta = betterproto.message_field(8, group="value")
    """duration specifies a value for a duration index field."""


class QueryStub(betterproto.ServiceStub):
    async def get(
        self,
        get_request: "GetRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetResponse":
        return await self._unary_unary(
            "/cosmos.orm.query.v1alpha1.Query/Get",
            get_request,
            GetResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def list(
        self,
        list_request: "ListRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "ListResponse":
        return await self._unary_unary(
            "/cosmos.orm.query.v1alpha1.Query/List",
            list_request,
            ListResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def get(self, get_request: "GetRequest") -> "GetResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list(self, list_request: "ListRequest") -> "ListResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get(
        self, stream: "grpclib.server.Stream[GetRequest, GetResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get(request)
        await stream.send_message(response)

    async def __rpc_list(
        self, stream: "grpclib.server.Stream[ListRequest, ListResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.list(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.orm.query.v1alpha1.Query/Get": grpclib.const.Handler(
                self.__rpc_get,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetRequest,
                GetResponse,
            ),
            "/cosmos.orm.query.v1alpha1.Query/List": grpclib.const.Handler(
                self.__rpc_list,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListRequest,
                ListResponse,
            ),
        }
