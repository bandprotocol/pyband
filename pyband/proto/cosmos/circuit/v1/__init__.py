# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/circuit/v1/query.proto, cosmos/circuit/v1/tx.proto, cosmos/circuit/v1/types.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...base.query import v1beta1 as __base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class PermissionsLevel(betterproto.Enum):
    """Level is the permission level."""

    LEVEL_NONE_UNSPECIFIED = 0
    """
    LEVEL_NONE_UNSPECIFIED indicates that the account will have no circuit
     breaker permissions.
    """

    LEVEL_SOME_MSGS = 1
    """
    LEVEL_SOME_MSGS indicates that the account will have permission to
     trip or reset the circuit breaker for some Msg type URLs. If this level
     is chosen, a non-empty list of Msg type URLs must be provided in
     limit_type_urls.
    """

    LEVEL_ALL_MSGS = 2
    """
    LEVEL_ALL_MSGS indicates that the account can trip or reset the circuit
     breaker for Msg's of all type URLs.
    """

    LEVEL_SUPER_ADMIN = 3
    """
    LEVEL_SUPER_ADMIN indicates that the account can take all circuit breaker
     actions and can grant permissions to other accounts.
    """


@dataclass(eq=False, repr=False)
class Permissions(betterproto.Message):
    """
    Permissions are the permissions that an account has to trip
     or reset the circuit breaker.
    """

    level: "PermissionsLevel" = betterproto.enum_field(1)
    """level is the level of permissions granted to this account."""

    limit_type_urls: List[str] = betterproto.string_field(2)
    """
    limit_type_urls is used with LEVEL_SOME_MSGS to limit the lists of Msg type
     URLs that the account can trip. It is an error to use limit_type_urls with
     a level other than LEVEL_SOME_MSGS.
    """


@dataclass(eq=False, repr=False)
class GenesisAccountPermissions(betterproto.Message):
    """
    GenesisAccountPermissions is the account permissions for the circuit breaker in genesis
    """

    address: str = betterproto.string_field(1)
    permissions: "Permissions" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState is the state that must be provided at genesis."""

    account_permissions: List["GenesisAccountPermissions"] = betterproto.message_field(
        1
    )
    disabled_type_urls: List[str] = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MsgAuthorizeCircuitBreaker(betterproto.Message):
    """
    MsgAuthorizeCircuitBreaker defines the Msg/AuthorizeCircuitBreaker request type.
    """

    granter: str = betterproto.string_field(1)
    """
    granter is the granter of the circuit breaker permissions and must have
     LEVEL_SUPER_ADMIN.
    """

    grantee: str = betterproto.string_field(2)
    """grantee is the account authorized with the provided permissions."""

    permissions: "Permissions" = betterproto.message_field(3)
    """
    permissions are the circuit breaker permissions that the grantee receives.
     These will overwrite any existing permissions. LEVEL_NONE_UNSPECIFIED can
     be specified to revoke all permissions.
    """


@dataclass(eq=False, repr=False)
class MsgAuthorizeCircuitBreakerResponse(betterproto.Message):
    """
    MsgAuthorizeCircuitBreakerResponse defines the Msg/AuthorizeCircuitBreaker response type.
    """

    success: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class MsgTripCircuitBreaker(betterproto.Message):
    """
    MsgTripCircuitBreaker defines the Msg/TripCircuitBreaker request type.
    """

    authority: str = betterproto.string_field(1)
    """authority is the account authorized to trip the circuit breaker."""

    msg_type_urls: List[str] = betterproto.string_field(2)
    """
    msg_type_urls specifies a list of type URLs to immediately stop processing.
     IF IT IS LEFT EMPTY, ALL MSG PROCESSING WILL STOP IMMEDIATELY.
     This value is validated against the authority's permissions and if the
     authority does not have permissions to trip the specified msg type URLs
     (or all URLs), the operation will fail.
    """


@dataclass(eq=False, repr=False)
class MsgTripCircuitBreakerResponse(betterproto.Message):
    """
    MsgTripCircuitBreakerResponse defines the Msg/TripCircuitBreaker response type.
    """

    success: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class MsgResetCircuitBreaker(betterproto.Message):
    """
    MsgResetCircuitBreaker defines the Msg/ResetCircuitBreaker request type.
    """

    authority: str = betterproto.string_field(1)
    """
    authority is the account authorized to trip or reset the circuit breaker.
    """

    msg_type_urls: List[str] = betterproto.string_field(3)
    """
    msg_type_urls specifies a list of Msg type URLs to resume processing. If
     it is left empty all Msg processing for type URLs that the account is
     authorized to trip will resume.
    """


@dataclass(eq=False, repr=False)
class MsgResetCircuitBreakerResponse(betterproto.Message):
    """
    MsgResetCircuitBreakerResponse defines the Msg/ResetCircuitBreaker response type.
    """

    success: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class QueryAccountRequest(betterproto.Message):
    """
    QueryAccountRequest is the request type for the Query/Account RPC method.
    """

    address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class AccountResponse(betterproto.Message):
    """
    AccountResponse is the response type for the Query/Account RPC method.
    """

    permission: "Permissions" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAccountsRequest(betterproto.Message):
    """
    QueryAccountsRequest is the request type for the Query/Accounts RPC method.
    """

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class AccountsResponse(betterproto.Message):
    """
    AccountsResponse is the response type for the Query/Accounts RPC method.
    """

    accounts: List["GenesisAccountPermissions"] = betterproto.message_field(1)
    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryDisabledListRequest(betterproto.Message):
    """
    QueryDisableListRequest is the request type for the Query/DisabledList RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class DisabledListResponse(betterproto.Message):
    """
    DisabledListResponse is the response type for the Query/DisabledList RPC method.
    """

    disabled_list: List[str] = betterproto.string_field(1)


class MsgStub(betterproto.ServiceStub):
    async def authorize_circuit_breaker(
        self,
        msg_authorize_circuit_breaker: "MsgAuthorizeCircuitBreaker",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgAuthorizeCircuitBreakerResponse":
        return await self._unary_unary(
            "/cosmos.circuit.v1.Msg/AuthorizeCircuitBreaker",
            msg_authorize_circuit_breaker,
            MsgAuthorizeCircuitBreakerResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def trip_circuit_breaker(
        self,
        msg_trip_circuit_breaker: "MsgTripCircuitBreaker",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgTripCircuitBreakerResponse":
        return await self._unary_unary(
            "/cosmos.circuit.v1.Msg/TripCircuitBreaker",
            msg_trip_circuit_breaker,
            MsgTripCircuitBreakerResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def reset_circuit_breaker(
        self,
        msg_reset_circuit_breaker: "MsgResetCircuitBreaker",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgResetCircuitBreakerResponse":
        return await self._unary_unary(
            "/cosmos.circuit.v1.Msg/ResetCircuitBreaker",
            msg_reset_circuit_breaker,
            MsgResetCircuitBreakerResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryStub(betterproto.ServiceStub):
    async def account(
        self,
        query_account_request: "QueryAccountRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "AccountResponse":
        return await self._unary_unary(
            "/cosmos.circuit.v1.Query/Account",
            query_account_request,
            AccountResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def accounts(
        self,
        query_accounts_request: "QueryAccountsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "AccountsResponse":
        return await self._unary_unary(
            "/cosmos.circuit.v1.Query/Accounts",
            query_accounts_request,
            AccountsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def disabled_list(
        self,
        query_disabled_list_request: "QueryDisabledListRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "DisabledListResponse":
        return await self._unary_unary(
            "/cosmos.circuit.v1.Query/DisabledList",
            query_disabled_list_request,
            DisabledListResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgBase(ServiceBase):

    async def authorize_circuit_breaker(
        self, msg_authorize_circuit_breaker: "MsgAuthorizeCircuitBreaker"
    ) -> "MsgAuthorizeCircuitBreakerResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def trip_circuit_breaker(
        self, msg_trip_circuit_breaker: "MsgTripCircuitBreaker"
    ) -> "MsgTripCircuitBreakerResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def reset_circuit_breaker(
        self, msg_reset_circuit_breaker: "MsgResetCircuitBreaker"
    ) -> "MsgResetCircuitBreakerResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_authorize_circuit_breaker(
        self,
        stream: "grpclib.server.Stream[MsgAuthorizeCircuitBreaker, MsgAuthorizeCircuitBreakerResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.authorize_circuit_breaker(request)
        await stream.send_message(response)

    async def __rpc_trip_circuit_breaker(
        self,
        stream: "grpclib.server.Stream[MsgTripCircuitBreaker, MsgTripCircuitBreakerResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.trip_circuit_breaker(request)
        await stream.send_message(response)

    async def __rpc_reset_circuit_breaker(
        self,
        stream: "grpclib.server.Stream[MsgResetCircuitBreaker, MsgResetCircuitBreakerResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.reset_circuit_breaker(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.circuit.v1.Msg/AuthorizeCircuitBreaker": grpclib.const.Handler(
                self.__rpc_authorize_circuit_breaker,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgAuthorizeCircuitBreaker,
                MsgAuthorizeCircuitBreakerResponse,
            ),
            "/cosmos.circuit.v1.Msg/TripCircuitBreaker": grpclib.const.Handler(
                self.__rpc_trip_circuit_breaker,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgTripCircuitBreaker,
                MsgTripCircuitBreakerResponse,
            ),
            "/cosmos.circuit.v1.Msg/ResetCircuitBreaker": grpclib.const.Handler(
                self.__rpc_reset_circuit_breaker,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgResetCircuitBreaker,
                MsgResetCircuitBreakerResponse,
            ),
        }


class QueryBase(ServiceBase):

    async def account(
        self, query_account_request: "QueryAccountRequest"
    ) -> "AccountResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def accounts(
        self, query_accounts_request: "QueryAccountsRequest"
    ) -> "AccountsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def disabled_list(
        self, query_disabled_list_request: "QueryDisabledListRequest"
    ) -> "DisabledListResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_account(
        self, stream: "grpclib.server.Stream[QueryAccountRequest, AccountResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.account(request)
        await stream.send_message(response)

    async def __rpc_accounts(
        self, stream: "grpclib.server.Stream[QueryAccountsRequest, AccountsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.accounts(request)
        await stream.send_message(response)

    async def __rpc_disabled_list(
        self,
        stream: "grpclib.server.Stream[QueryDisabledListRequest, DisabledListResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.disabled_list(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.circuit.v1.Query/Account": grpclib.const.Handler(
                self.__rpc_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountRequest,
                AccountResponse,
            ),
            "/cosmos.circuit.v1.Query/Accounts": grpclib.const.Handler(
                self.__rpc_accounts,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountsRequest,
                AccountsResponse,
            ),
            "/cosmos.circuit.v1.Query/DisabledList": grpclib.const.Handler(
                self.__rpc_disabled_list,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDisabledListRequest,
                DisabledListResponse,
            ),
        }
