"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BitArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BITS_FIELD_NUMBER: builtins.int
    ELEMS_FIELD_NUMBER: builtins.int
    bits: builtins.int = ...

    @property
    def elems(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...

    def __init__(self,
        *,
        bits : builtins.int = ...,
        elems : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bits",b"bits",u"elems",b"elems"]) -> None: ...
global___BitArray = BitArray