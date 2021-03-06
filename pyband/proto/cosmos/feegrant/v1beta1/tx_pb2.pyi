"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# MsgGrantAllowance adds permission for Grantee to spend up to Allowance
# of fees from the account of Granter.
class MsgGrantAllowance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    ALLOWANCE_FIELD_NUMBER: builtins.int
    # granter is the address of the user granting an allowance of their funds.
    granter: typing.Text = ...
    # grantee is the address of the user being granted an allowance of another user's funds.
    grantee: typing.Text = ...
    # allowance can be any of basic and filtered fee allowance.
    @property
    def allowance(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(self,
        *,
        granter : typing.Text = ...,
        grantee : typing.Text = ...,
        allowance : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"allowance",b"allowance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"allowance",b"allowance",u"grantee",b"grantee",u"granter",b"granter"]) -> None: ...
global___MsgGrantAllowance = MsgGrantAllowance

# MsgGrantAllowanceResponse defines the Msg/GrantAllowanceResponse response type.
class MsgGrantAllowanceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgGrantAllowanceResponse = MsgGrantAllowanceResponse

# MsgRevokeAllowance removes any existing Allowance from Granter to Grantee.
class MsgRevokeAllowance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    # granter is the address of the user granting an allowance of their funds.
    granter: typing.Text = ...
    # grantee is the address of the user being granted an allowance of another user's funds.
    grantee: typing.Text = ...
    def __init__(self,
        *,
        granter : typing.Text = ...,
        grantee : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"grantee",b"grantee",u"granter",b"granter"]) -> None: ...
global___MsgRevokeAllowance = MsgRevokeAllowance

# MsgRevokeAllowanceResponse defines the Msg/RevokeAllowanceResponse response type.
class MsgRevokeAllowanceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgRevokeAllowanceResponse = MsgRevokeAllowanceResponse
