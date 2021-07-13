"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MsgSetWithdrawAddress(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    WITHDRAW_ADDRESS_FIELD_NUMBER: builtins.int
    delegator_address: typing.Text = ...
    withdraw_address: typing.Text = ...

    def __init__(self,
        *,
        delegator_address : typing.Text = ...,
        withdraw_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_address",b"delegator_address",u"withdraw_address",b"withdraw_address"]) -> None: ...
global___MsgSetWithdrawAddress = MsgSetWithdrawAddress

class MsgSetWithdrawAddressResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___MsgSetWithdrawAddressResponse = MsgSetWithdrawAddressResponse

class MsgWithdrawDelegatorReward(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    delegator_address: typing.Text = ...
    validator_address: typing.Text = ...

    def __init__(self,
        *,
        delegator_address : typing.Text = ...,
        validator_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_address",b"delegator_address",u"validator_address",b"validator_address"]) -> None: ...
global___MsgWithdrawDelegatorReward = MsgWithdrawDelegatorReward

class MsgWithdrawDelegatorRewardResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___MsgWithdrawDelegatorRewardResponse = MsgWithdrawDelegatorRewardResponse

class MsgWithdrawValidatorCommission(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    validator_address: typing.Text = ...

    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validator_address",b"validator_address"]) -> None: ...
global___MsgWithdrawValidatorCommission = MsgWithdrawValidatorCommission

class MsgWithdrawValidatorCommissionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___MsgWithdrawValidatorCommissionResponse = MsgWithdrawValidatorCommissionResponse

class MsgFundCommunityPool(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AMOUNT_FIELD_NUMBER: builtins.int
    DEPOSITOR_FIELD_NUMBER: builtins.int
    depositor: typing.Text = ...

    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...

    def __init__(self,
        *,
        amount : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        depositor : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"amount",b"amount",u"depositor",b"depositor"]) -> None: ...
global___MsgFundCommunityPool = MsgFundCommunityPool

class MsgFundCommunityPoolResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___MsgFundCommunityPoolResponse = MsgFundCommunityPoolResponse