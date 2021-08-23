"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.staking.v1beta1.staking_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class QueryValidatorsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    status: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        status : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"status",b"status"]) -> None: ...
global___QueryValidatorsRequest = QueryValidatorsRequest

class QueryValidatorsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATORS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.Validator]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        validators : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.Validator]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"validators",b"validators"]) -> None: ...
global___QueryValidatorsResponse = QueryValidatorsResponse

class QueryValidatorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    validator_addr: typing.Text = ...

    def __init__(self,
        *,
        validator_addr : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validator_addr",b"validator_addr"]) -> None: ...
global___QueryValidatorRequest = QueryValidatorRequest

class QueryValidatorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_FIELD_NUMBER: builtins.int

    @property
    def validator(self) -> cosmos.staking.v1beta1.staking_pb2.Validator: ...

    def __init__(self,
        *,
        validator : typing.Optional[cosmos.staking.v1beta1.staking_pb2.Validator] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"validator",b"validator"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validator",b"validator"]) -> None: ...
global___QueryValidatorResponse = QueryValidatorResponse

class QueryValidatorDelegationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    validator_addr: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        validator_addr : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"validator_addr",b"validator_addr"]) -> None: ...
global___QueryValidatorDelegationsRequest = QueryValidatorDelegationsRequest

class QueryValidatorDelegationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATION_RESPONSES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def delegation_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.DelegationResponse]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        delegation_responses : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.DelegationResponse]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegation_responses",b"delegation_responses",u"pagination",b"pagination"]) -> None: ...
global___QueryValidatorDelegationsResponse = QueryValidatorDelegationsResponse

class QueryValidatorUnbondingDelegationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    validator_addr: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        validator_addr : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"validator_addr",b"validator_addr"]) -> None: ...
global___QueryValidatorUnbondingDelegationsRequest = QueryValidatorUnbondingDelegationsRequest

class QueryValidatorUnbondingDelegationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNBONDING_RESPONSES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def unbonding_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        unbonding_responses : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"unbonding_responses",b"unbonding_responses"]) -> None: ...
global___QueryValidatorUnbondingDelegationsResponse = QueryValidatorUnbondingDelegationsResponse

class QueryDelegationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDR_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    delegator_addr: typing.Text = ...
    validator_addr: typing.Text = ...

    def __init__(self,
        *,
        delegator_addr : typing.Text = ...,
        validator_addr : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_addr",b"delegator_addr",u"validator_addr",b"validator_addr"]) -> None: ...
global___QueryDelegationRequest = QueryDelegationRequest

class QueryDelegationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATION_RESPONSE_FIELD_NUMBER: builtins.int

    @property
    def delegation_response(self) -> cosmos.staking.v1beta1.staking_pb2.DelegationResponse: ...

    def __init__(self,
        *,
        delegation_response : typing.Optional[cosmos.staking.v1beta1.staking_pb2.DelegationResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"delegation_response",b"delegation_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegation_response",b"delegation_response"]) -> None: ...
global___QueryDelegationResponse = QueryDelegationResponse

class QueryUnbondingDelegationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDR_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    delegator_addr: typing.Text = ...
    validator_addr: typing.Text = ...

    def __init__(self,
        *,
        delegator_addr : typing.Text = ...,
        validator_addr : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_addr",b"delegator_addr",u"validator_addr",b"validator_addr"]) -> None: ...
global___QueryUnbondingDelegationRequest = QueryUnbondingDelegationRequest

class QueryUnbondingDelegationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNBOND_FIELD_NUMBER: builtins.int

    @property
    def unbond(self) -> cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation: ...

    def __init__(self,
        *,
        unbond : typing.Optional[cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"unbond",b"unbond"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"unbond",b"unbond"]) -> None: ...
global___QueryUnbondingDelegationResponse = QueryUnbondingDelegationResponse

class QueryDelegatorDelegationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDR_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    delegator_addr: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        delegator_addr : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_addr",b"delegator_addr",u"pagination",b"pagination"]) -> None: ...
global___QueryDelegatorDelegationsRequest = QueryDelegatorDelegationsRequest

class QueryDelegatorDelegationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATION_RESPONSES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def delegation_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.DelegationResponse]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        delegation_responses : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.DelegationResponse]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegation_responses",b"delegation_responses",u"pagination",b"pagination"]) -> None: ...
global___QueryDelegatorDelegationsResponse = QueryDelegatorDelegationsResponse

class QueryDelegatorUnbondingDelegationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDR_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    delegator_addr: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        delegator_addr : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_addr",b"delegator_addr",u"pagination",b"pagination"]) -> None: ...
global___QueryDelegatorUnbondingDelegationsRequest = QueryDelegatorUnbondingDelegationsRequest

class QueryDelegatorUnbondingDelegationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNBONDING_RESPONSES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def unbonding_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        unbonding_responses : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.UnbondingDelegation]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"unbonding_responses",b"unbonding_responses"]) -> None: ...
global___QueryDelegatorUnbondingDelegationsResponse = QueryDelegatorUnbondingDelegationsResponse

class QueryRedelegationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDR_FIELD_NUMBER: builtins.int
    SRC_VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    DST_VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    delegator_addr: typing.Text = ...
    src_validator_addr: typing.Text = ...
    dst_validator_addr: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        delegator_addr : typing.Text = ...,
        src_validator_addr : typing.Text = ...,
        dst_validator_addr : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_addr",b"delegator_addr",u"dst_validator_addr",b"dst_validator_addr",u"pagination",b"pagination",u"src_validator_addr",b"src_validator_addr"]) -> None: ...
global___QueryRedelegationsRequest = QueryRedelegationsRequest

class QueryRedelegationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REDELEGATION_RESPONSES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def redelegation_responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.RedelegationResponse]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        redelegation_responses : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.RedelegationResponse]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"redelegation_responses",b"redelegation_responses"]) -> None: ...
global___QueryRedelegationsResponse = QueryRedelegationsResponse

class QueryDelegatorValidatorsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDR_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    delegator_addr: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        delegator_addr : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_addr",b"delegator_addr",u"pagination",b"pagination"]) -> None: ...
global___QueryDelegatorValidatorsRequest = QueryDelegatorValidatorsRequest

class QueryDelegatorValidatorsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATORS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.Validator]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        validators : typing.Optional[typing.Iterable[cosmos.staking.v1beta1.staking_pb2.Validator]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination",u"validators",b"validators"]) -> None: ...
global___QueryDelegatorValidatorsResponse = QueryDelegatorValidatorsResponse

class QueryDelegatorValidatorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDR_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    delegator_addr: typing.Text = ...
    validator_addr: typing.Text = ...

    def __init__(self,
        *,
        delegator_addr : typing.Text = ...,
        validator_addr : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_addr",b"delegator_addr",u"validator_addr",b"validator_addr"]) -> None: ...
global___QueryDelegatorValidatorRequest = QueryDelegatorValidatorRequest

class QueryDelegatorValidatorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_FIELD_NUMBER: builtins.int

    @property
    def validator(self) -> cosmos.staking.v1beta1.staking_pb2.Validator: ...

    def __init__(self,
        *,
        validator : typing.Optional[cosmos.staking.v1beta1.staking_pb2.Validator] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"validator",b"validator"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validator",b"validator"]) -> None: ...
global___QueryDelegatorValidatorResponse = QueryDelegatorValidatorResponse

class QueryHistoricalInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HEIGHT_FIELD_NUMBER: builtins.int
    height: builtins.int = ...

    def __init__(self,
        *,
        height : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"height",b"height"]) -> None: ...
global___QueryHistoricalInfoRequest = QueryHistoricalInfoRequest

class QueryHistoricalInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HIST_FIELD_NUMBER: builtins.int

    @property
    def hist(self) -> cosmos.staking.v1beta1.staking_pb2.HistoricalInfo: ...

    def __init__(self,
        *,
        hist : typing.Optional[cosmos.staking.v1beta1.staking_pb2.HistoricalInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"hist",b"hist"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hist",b"hist"]) -> None: ...
global___QueryHistoricalInfoResponse = QueryHistoricalInfoResponse

class QueryPoolRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___QueryPoolRequest = QueryPoolRequest

class QueryPoolResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    POOL_FIELD_NUMBER: builtins.int

    @property
    def pool(self) -> cosmos.staking.v1beta1.staking_pb2.Pool: ...

    def __init__(self,
        *,
        pool : typing.Optional[cosmos.staking.v1beta1.staking_pb2.Pool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pool",b"pool"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pool",b"pool"]) -> None: ...
global___QueryPoolResponse = QueryPoolResponse

class QueryParamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARAMS_FIELD_NUMBER: builtins.int

    @property
    def params(self) -> cosmos.staking.v1beta1.staking_pb2.Params: ...

    def __init__(self,
        *,
        params : typing.Optional[cosmos.staking.v1beta1.staking_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> None: ...
global___QueryParamsResponse = QueryParamsResponse