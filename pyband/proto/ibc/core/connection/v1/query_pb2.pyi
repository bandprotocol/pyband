"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ibc.core.client.v1.client_pb2
import ibc.core.connection.v1.connection_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# QueryConnectionRequest is the request type for the Query/Connection RPC
# method
class QueryConnectionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    # connection unique identifier
    connection_id: typing.Text = ...
    def __init__(self,
        *,
        connection_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connection_id",b"connection_id"]) -> None: ...
global___QueryConnectionRequest = QueryConnectionRequest

# QueryConnectionResponse is the response type for the Query/Connection RPC
# method. Besides the connection end, it includes a proof and the height from
# which the proof was retrieved.
class QueryConnectionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    # connection associated with the request identifier
    @property
    def connection(self) -> ibc.core.connection.v1.connection_pb2.ConnectionEnd: ...
    # merkle proof of existence
    proof: builtins.bytes = ...
    # height at which the proof was retrieved
    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    def __init__(self,
        *,
        connection : typing.Optional[ibc.core.connection.v1.connection_pb2.ConnectionEnd] = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"connection",b"connection",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connection",b"connection",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryConnectionResponse = QueryConnectionResponse

# QueryConnectionsRequest is the request type for the Query/Connections RPC
# method
class QueryConnectionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(self,
        *,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> None: ...
global___QueryConnectionsRequest = QueryConnectionsRequest

# QueryConnectionsResponse is the response type for the Query/Connections RPC
# method.
class QueryConnectionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTIONS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    # list of stored connections of the chain.
    @property
    def connections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.connection.v1.connection_pb2.IdentifiedConnection]: ...
    # pagination response
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    # query block height
    @property
    def height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    def __init__(self,
        *,
        connections : typing.Optional[typing.Iterable[ibc.core.connection.v1.connection_pb2.IdentifiedConnection]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"height",b"height",u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connections",b"connections",u"height",b"height",u"pagination",b"pagination"]) -> None: ...
global___QueryConnectionsResponse = QueryConnectionsResponse

# QueryClientConnectionsRequest is the request type for the
# Query/ClientConnections RPC method
class QueryClientConnectionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    # client identifier associated with a connection
    client_id: typing.Text = ...
    def __init__(self,
        *,
        client_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id"]) -> None: ...
global___QueryClientConnectionsRequest = QueryClientConnectionsRequest

# QueryClientConnectionsResponse is the response type for the
# Query/ClientConnections RPC method
class QueryClientConnectionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_PATHS_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    # slice of all the connection paths associated with a client.
    @property
    def connection_paths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    # merkle proof of existence
    proof: builtins.bytes = ...
    # height at which the proof was generated
    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    def __init__(self,
        *,
        connection_paths : typing.Optional[typing.Iterable[typing.Text]] = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connection_paths",b"connection_paths",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryClientConnectionsResponse = QueryClientConnectionsResponse

# QueryConnectionClientStateRequest is the request type for the
# Query/ConnectionClientState RPC method
class QueryConnectionClientStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    # connection identifier
    connection_id: typing.Text = ...
    def __init__(self,
        *,
        connection_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connection_id",b"connection_id"]) -> None: ...
global___QueryConnectionClientStateRequest = QueryConnectionClientStateRequest

# QueryConnectionClientStateResponse is the response type for the
# Query/ConnectionClientState RPC method
class QueryConnectionClientStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IDENTIFIED_CLIENT_STATE_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    # client state associated with the channel
    @property
    def identified_client_state(self) -> ibc.core.client.v1.client_pb2.IdentifiedClientState: ...
    # merkle proof of existence
    proof: builtins.bytes = ...
    # height at which the proof was retrieved
    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    def __init__(self,
        *,
        identified_client_state : typing.Optional[ibc.core.client.v1.client_pb2.IdentifiedClientState] = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"identified_client_state",b"identified_client_state",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"identified_client_state",b"identified_client_state",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryConnectionClientStateResponse = QueryConnectionClientStateResponse

# QueryConnectionConsensusStateRequest is the request type for the
# Query/ConnectionConsensusState RPC method
class QueryConnectionConsensusStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    REVISION_NUMBER_FIELD_NUMBER: builtins.int
    REVISION_HEIGHT_FIELD_NUMBER: builtins.int
    # connection identifier
    connection_id: typing.Text = ...
    revision_number: builtins.int = ...
    revision_height: builtins.int = ...
    def __init__(self,
        *,
        connection_id : typing.Text = ...,
        revision_number : builtins.int = ...,
        revision_height : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connection_id",b"connection_id",u"revision_height",b"revision_height",u"revision_number",b"revision_number"]) -> None: ...
global___QueryConnectionConsensusStateRequest = QueryConnectionConsensusStateRequest

# QueryConnectionConsensusStateResponse is the response type for the
# Query/ConnectionConsensusState RPC method
class QueryConnectionConsensusStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSENSUS_STATE_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    # consensus state associated with the channel
    @property
    def consensus_state(self) -> google.protobuf.any_pb2.Any: ...
    # client ID associated with the consensus state
    client_id: typing.Text = ...
    # merkle proof of existence
    proof: builtins.bytes = ...
    # height at which the proof was retrieved
    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    def __init__(self,
        *,
        consensus_state : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        client_id : typing.Text = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"consensus_state",b"consensus_state",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"consensus_state",b"consensus_state",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryConnectionConsensusStateResponse = QueryConnectionConsensusStateResponse
