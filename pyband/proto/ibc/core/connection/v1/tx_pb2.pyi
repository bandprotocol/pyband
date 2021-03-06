"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ibc.core.client.v1.client_pb2
import ibc.core.connection.v1.connection_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# MsgConnectionOpenInit defines the msg sent by an account on Chain A to
# initialize a connection with Chain B.
class MsgConnectionOpenInit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    COUNTERPARTY_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    DELAY_PERIOD_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...
    @property
    def counterparty(self) -> ibc.core.connection.v1.connection_pb2.Counterparty: ...
    @property
    def version(self) -> ibc.core.connection.v1.connection_pb2.Version: ...
    delay_period: builtins.int = ...
    signer: typing.Text = ...
    def __init__(self,
        *,
        client_id : typing.Text = ...,
        counterparty : typing.Optional[ibc.core.connection.v1.connection_pb2.Counterparty] = ...,
        version : typing.Optional[ibc.core.connection.v1.connection_pb2.Version] = ...,
        delay_period : builtins.int = ...,
        signer : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"counterparty",b"counterparty",u"version",b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"counterparty",b"counterparty",u"delay_period",b"delay_period",u"signer",b"signer",u"version",b"version"]) -> None: ...
global___MsgConnectionOpenInit = MsgConnectionOpenInit

# MsgConnectionOpenInitResponse defines the Msg/ConnectionOpenInit response
# type.
class MsgConnectionOpenInitResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgConnectionOpenInitResponse = MsgConnectionOpenInitResponse

# MsgConnectionOpenTry defines a msg sent by a Relayer to try to open a
# connection on Chain B.
class MsgConnectionOpenTry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    PREVIOUS_CONNECTION_ID_FIELD_NUMBER: builtins.int
    CLIENT_STATE_FIELD_NUMBER: builtins.int
    COUNTERPARTY_FIELD_NUMBER: builtins.int
    DELAY_PERIOD_FIELD_NUMBER: builtins.int
    COUNTERPARTY_VERSIONS_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    PROOF_INIT_FIELD_NUMBER: builtins.int
    PROOF_CLIENT_FIELD_NUMBER: builtins.int
    PROOF_CONSENSUS_FIELD_NUMBER: builtins.int
    CONSENSUS_HEIGHT_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...
    # in the case of crossing hello's, when both chains call OpenInit, we need
    # the connection identifier of the previous connection in state INIT
    previous_connection_id: typing.Text = ...
    @property
    def client_state(self) -> google.protobuf.any_pb2.Any: ...
    @property
    def counterparty(self) -> ibc.core.connection.v1.connection_pb2.Counterparty: ...
    delay_period: builtins.int = ...
    @property
    def counterparty_versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.connection.v1.connection_pb2.Version]: ...
    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    # proof of the initialization the connection on Chain A: `UNITIALIZED ->
    # INIT`
    proof_init: builtins.bytes = ...
    # proof of client state included in message
    proof_client: builtins.bytes = ...
    # proof of client consensus state
    proof_consensus: builtins.bytes = ...
    @property
    def consensus_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    signer: typing.Text = ...
    def __init__(self,
        *,
        client_id : typing.Text = ...,
        previous_connection_id : typing.Text = ...,
        client_state : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        counterparty : typing.Optional[ibc.core.connection.v1.connection_pb2.Counterparty] = ...,
        delay_period : builtins.int = ...,
        counterparty_versions : typing.Optional[typing.Iterable[ibc.core.connection.v1.connection_pb2.Version]] = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        proof_init : builtins.bytes = ...,
        proof_client : builtins.bytes = ...,
        proof_consensus : builtins.bytes = ...,
        consensus_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        signer : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"client_state",b"client_state",u"consensus_height",b"consensus_height",u"counterparty",b"counterparty",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"client_state",b"client_state",u"consensus_height",b"consensus_height",u"counterparty",b"counterparty",u"counterparty_versions",b"counterparty_versions",u"delay_period",b"delay_period",u"previous_connection_id",b"previous_connection_id",u"proof_client",b"proof_client",u"proof_consensus",b"proof_consensus",u"proof_height",b"proof_height",u"proof_init",b"proof_init",u"signer",b"signer"]) -> None: ...
global___MsgConnectionOpenTry = MsgConnectionOpenTry

# MsgConnectionOpenTryResponse defines the Msg/ConnectionOpenTry response type.
class MsgConnectionOpenTryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgConnectionOpenTryResponse = MsgConnectionOpenTryResponse

# MsgConnectionOpenAck defines a msg sent by a Relayer to Chain A to
# acknowledge the change of connection state to TRYOPEN on Chain B.
class MsgConnectionOpenAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    COUNTERPARTY_CONNECTION_ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    CLIENT_STATE_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    PROOF_TRY_FIELD_NUMBER: builtins.int
    PROOF_CLIENT_FIELD_NUMBER: builtins.int
    PROOF_CONSENSUS_FIELD_NUMBER: builtins.int
    CONSENSUS_HEIGHT_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    connection_id: typing.Text = ...
    counterparty_connection_id: typing.Text = ...
    @property
    def version(self) -> ibc.core.connection.v1.connection_pb2.Version: ...
    @property
    def client_state(self) -> google.protobuf.any_pb2.Any: ...
    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    # proof of the initialization the connection on Chain B: `UNITIALIZED ->
    # TRYOPEN`
    proof_try: builtins.bytes = ...
    # proof of client state included in message
    proof_client: builtins.bytes = ...
    # proof of client consensus state
    proof_consensus: builtins.bytes = ...
    @property
    def consensus_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    signer: typing.Text = ...
    def __init__(self,
        *,
        connection_id : typing.Text = ...,
        counterparty_connection_id : typing.Text = ...,
        version : typing.Optional[ibc.core.connection.v1.connection_pb2.Version] = ...,
        client_state : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        proof_try : builtins.bytes = ...,
        proof_client : builtins.bytes = ...,
        proof_consensus : builtins.bytes = ...,
        consensus_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        signer : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"client_state",b"client_state",u"consensus_height",b"consensus_height",u"proof_height",b"proof_height",u"version",b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_state",b"client_state",u"connection_id",b"connection_id",u"consensus_height",b"consensus_height",u"counterparty_connection_id",b"counterparty_connection_id",u"proof_client",b"proof_client",u"proof_consensus",b"proof_consensus",u"proof_height",b"proof_height",u"proof_try",b"proof_try",u"signer",b"signer",u"version",b"version"]) -> None: ...
global___MsgConnectionOpenAck = MsgConnectionOpenAck

# MsgConnectionOpenAckResponse defines the Msg/ConnectionOpenAck response type.
class MsgConnectionOpenAckResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgConnectionOpenAckResponse = MsgConnectionOpenAckResponse

# MsgConnectionOpenConfirm defines a msg sent by a Relayer to Chain B to
# acknowledge the change of connection state to OPEN on Chain A.
class MsgConnectionOpenConfirm(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_ID_FIELD_NUMBER: builtins.int
    PROOF_ACK_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    SIGNER_FIELD_NUMBER: builtins.int
    connection_id: typing.Text = ...
    # proof for the change of the connection state on Chain A: `INIT -> OPEN`
    proof_ack: builtins.bytes = ...
    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    signer: typing.Text = ...
    def __init__(self,
        *,
        connection_id : typing.Text = ...,
        proof_ack : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        signer : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connection_id",b"connection_id",u"proof_ack",b"proof_ack",u"proof_height",b"proof_height",u"signer",b"signer"]) -> None: ...
global___MsgConnectionOpenConfirm = MsgConnectionOpenConfirm

# MsgConnectionOpenConfirmResponse defines the Msg/ConnectionOpenConfirm
# response type.
class MsgConnectionOpenConfirmResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgConnectionOpenConfirmResponse = MsgConnectionOpenConfirmResponse
