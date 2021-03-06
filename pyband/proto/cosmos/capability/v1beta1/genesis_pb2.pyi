"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.capability.v1beta1.capability_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# GenesisOwners defines the capability owners with their corresponding index.
class GenesisOwners(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INDEX_FIELD_NUMBER: builtins.int
    INDEX_OWNERS_FIELD_NUMBER: builtins.int
    # index is the index of the capability owner.
    index: builtins.int = ...
    # index_owners are the owners at the given index.
    @property
    def index_owners(self) -> cosmos.capability.v1beta1.capability_pb2.CapabilityOwners: ...
    def __init__(self,
        *,
        index : builtins.int = ...,
        index_owners : typing.Optional[cosmos.capability.v1beta1.capability_pb2.CapabilityOwners] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"index_owners",b"index_owners"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"index",b"index",u"index_owners",b"index_owners"]) -> None: ...
global___GenesisOwners = GenesisOwners

# GenesisState defines the capability module's genesis state.
class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INDEX_FIELD_NUMBER: builtins.int
    OWNERS_FIELD_NUMBER: builtins.int
    # index is the capability global index.
    index: builtins.int = ...
    # owners represents a map from index to owners of the capability index
    # index key is string to allow amino marshalling.
    @property
    def owners(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GenesisOwners]: ...
    def __init__(self,
        *,
        index : builtins.int = ...,
        owners : typing.Optional[typing.Iterable[global___GenesisOwners]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"index",b"index",u"owners",b"owners"]) -> None: ...
global___GenesisState = GenesisState
