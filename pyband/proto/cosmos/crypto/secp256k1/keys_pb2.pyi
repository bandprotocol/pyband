"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PubKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    key: builtins.bytes = ...

    def __init__(self,
        *,
        key : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key"]) -> None: ...
global___PubKey = PubKey

class PrivKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    key: builtins.bytes = ...

    def __init__(self,
        *,
        key : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key"]) -> None: ...
global___PrivKey = PrivKey