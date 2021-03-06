"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# GenesisState defines the authz module's genesis state.
class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AUTHORIZATION_FIELD_NUMBER: builtins.int
    @property
    def authorization(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrantAuthorization]: ...
    def __init__(self,
        *,
        authorization : typing.Optional[typing.Iterable[global___GrantAuthorization]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"authorization",b"authorization"]) -> None: ...
global___GenesisState = GenesisState

# GrantAuthorization defines the GenesisState/GrantAuthorization type.
class GrantAuthorization(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    AUTHORIZATION_FIELD_NUMBER: builtins.int
    EXPIRATION_FIELD_NUMBER: builtins.int
    granter: typing.Text = ...
    grantee: typing.Text = ...
    @property
    def authorization(self) -> google.protobuf.any_pb2.Any: ...
    @property
    def expiration(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        granter : typing.Text = ...,
        grantee : typing.Text = ...,
        authorization : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        expiration : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"authorization",b"authorization",u"expiration",b"expiration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"authorization",b"authorization",u"expiration",b"expiration",u"grantee",b"grantee",u"granter",b"granter"]) -> None: ...
global___GrantAuthorization = GrantAuthorization
