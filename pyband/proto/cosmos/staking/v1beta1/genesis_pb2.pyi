"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.staking.v1beta1.staking_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# GenesisState defines the staking module's genesis state.
class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARAMS_FIELD_NUMBER: builtins.int
    LAST_TOTAL_POWER_FIELD_NUMBER: builtins.int
    LAST_VALIDATOR_POWERS_FIELD_NUMBER: builtins.int
    VALIDATORS_FIELD_NUMBER: builtins.int
    DELEGATIONS_FIELD_NUMBER: builtins.int
    UNBONDING_DELEGATIONS_FIELD_NUMBER: builtins.int
    REDELEGATIONS_FIELD_NUMBER: builtins.int
    EXPORTED_FIELD_NUMBER: builtins.int
    # params defines all the paramaters of related to deposit.
    @property
    def params(self) -> cosmos.staking.v1beta1.staking_pb2.Params: ...
    # last_total_power tracks the total amounts of bonded tokens recorded during
    # the previous end block.
    last_total_power: builtins.bytes = ...
    # last_validator_powers is a special index that provides a historical list
    # of the last-block's bonded validators.
    @property
    def last_validator_powers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LastValidatorPower]: ...
    # delegations defines the validator set at genesis.
    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.Validator]: ...
    # delegations defines the delegations active at genesis.
    @property
    def delegations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.Delegation]: ...
    # unbonding_delegations defines the unbonding delegations active at genesis.
    @property
    def unbonding_delegations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation]: ...
    # redelegations defines the redelegations active at genesis.
    @property
    def redelegations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.Redelegation]: ...
    exported: builtins.bool = ...
    def __init__(self,
        *,
        params : typing.Optional[cosmos.staking.v1beta1.staking_pb2.Params] = ...,
        last_total_power : builtins.bytes = ...,
        last_validator_powers : typing.Optional[typing.Iterable[global___LastValidatorPower]] = ...,
        validators : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.Validator]] = ...,
        delegations : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.Delegation]] = ...,
        unbonding_delegations : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation]] = ...,
        redelegations : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.Redelegation]] = ...,
        exported : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegations",b"delegations",u"exported",b"exported",u"last_total_power",b"last_total_power",u"last_validator_powers",b"last_validator_powers",u"params",b"params",u"redelegations",b"redelegations",u"unbonding_delegations",b"unbonding_delegations",u"validators",b"validators"]) -> None: ...
global___GenesisState = GenesisState

# LastValidatorPower required for validator set update logic.
class LastValidatorPower(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    POWER_FIELD_NUMBER: builtins.int
    # address is the address of the validator.
    address: typing.Text = ...
    # power defines the power of the validator.
    power: builtins.int = ...
    def __init__(self,
        *,
        address : typing.Text = ...,
        power : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"power",b"power"]) -> None: ...
global___LastValidatorPower = LastValidatorPower
