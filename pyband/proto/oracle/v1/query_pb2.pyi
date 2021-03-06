"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import oracle.v1.oracle_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# QueryCountsRequest is request type for the Query/Count RPC method.
class QueryCountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___QueryCountsRequest = QueryCountsRequest

# QueryCountsResponse is response type for the Query/Count RPC method.
class QueryCountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_SOURCE_COUNT_FIELD_NUMBER: builtins.int
    ORACLE_SCRIPT_COUNT_FIELD_NUMBER: builtins.int
    REQUEST_COUNT_FIELD_NUMBER: builtins.int
    # DataSourceCount is total number of data sources available on the chain
    data_source_count: builtins.int = ...
    # OracleScriptCount is total number of oracle scripts available on the chain
    oracle_script_count: builtins.int = ...
    # RequestCount is total number of requests submitted to the chain
    request_count: builtins.int = ...
    def __init__(self,
        *,
        data_source_count : builtins.int = ...,
        oracle_script_count : builtins.int = ...,
        request_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data_source_count",b"data_source_count",u"oracle_script_count",b"oracle_script_count",u"request_count",b"request_count"]) -> None: ...
global___QueryCountsResponse = QueryCountsResponse

# QueryDataRequest is request type for the Query/Data RPC method.
class QueryDataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_HASH_FIELD_NUMBER: builtins.int
    # DataHash is SHA256 hash of the file's content, which can be data source or
    # oracle script
    data_hash: typing.Text = ...
    def __init__(self,
        *,
        data_hash : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data_hash",b"data_hash"]) -> None: ...
global___QueryDataRequest = QueryDataRequest

# QueryDataResponse is response type for the Query/Data RPC method.
class QueryDataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_FIELD_NUMBER: builtins.int
    # Data is file's content, which can be data source or oracle script
    data: builtins.bytes = ...
    def __init__(self,
        *,
        data : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data",b"data"]) -> None: ...
global___QueryDataResponse = QueryDataResponse

# QueryDataSourceRequest is request type for the Query/DataSource RPC method.
class QueryDataSourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_SOURCE_ID_FIELD_NUMBER: builtins.int
    # DataSourceID is ID of a data source script
    data_source_id: builtins.int = ...
    def __init__(self,
        *,
        data_source_id : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data_source_id",b"data_source_id"]) -> None: ...
global___QueryDataSourceRequest = QueryDataSourceRequest

# QueryDataSourceResponse is response type for the Query/DataSource RPC method.
class QueryDataSourceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_SOURCE_FIELD_NUMBER: builtins.int
    # DataSource is summary information of a data source
    @property
    def data_source(self) -> oracle.v1.oracle_pb2.DataSource: ...
    def __init__(self,
        *,
        data_source : typing.Optional[oracle.v1.oracle_pb2.DataSource] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"data_source",b"data_source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data_source",b"data_source"]) -> None: ...
global___QueryDataSourceResponse = QueryDataSourceResponse

# QueryOracleScriptRequest is request type for the Query/OracleScript RPC
# method.
class QueryOracleScriptRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ORACLE_SCRIPT_ID_FIELD_NUMBER: builtins.int
    # OracleScriptID is ID of an oracle script
    oracle_script_id: builtins.int = ...
    def __init__(self,
        *,
        oracle_script_id : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"oracle_script_id",b"oracle_script_id"]) -> None: ...
global___QueryOracleScriptRequest = QueryOracleScriptRequest

# QueryOracleScriptResponse is response type for the Query/OracleScript RPC
# method.
class QueryOracleScriptResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ORACLE_SCRIPT_FIELD_NUMBER: builtins.int
    # OracleScript is summary information of an oracle script
    @property
    def oracle_script(self) -> oracle.v1.oracle_pb2.OracleScript: ...
    def __init__(self,
        *,
        oracle_script : typing.Optional[oracle.v1.oracle_pb2.OracleScript] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"oracle_script",b"oracle_script"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"oracle_script",b"oracle_script"]) -> None: ...
global___QueryOracleScriptResponse = QueryOracleScriptResponse

# QueryRequestRequest is request type for the Query/Request RPC method.
class QueryRequestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REQUEST_ID_FIELD_NUMBER: builtins.int
    # RequestID is ID of an oracle request
    request_id: builtins.int = ...
    def __init__(self,
        *,
        request_id : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"request_id",b"request_id"]) -> None: ...
global___QueryRequestRequest = QueryRequestRequest

# QueryRequestResponse is response type for the Query/Request RPC method.
class QueryRequestResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REQUEST_FIELD_NUMBER: builtins.int
    REPORTS_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    # Request is an oracle request
    @property
    def request(self) -> oracle.v1.oracle_pb2.Request: ...
    # Reports is list of result data as raw reports that are fulfilled by
    # assigned validators
    @property
    def reports(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[oracle.v1.oracle_pb2.Report]: ...
    # Result is a final form of result data
    @property
    def result(self) -> oracle.v1.oracle_pb2.Result: ...
    def __init__(self,
        *,
        request : typing.Optional[oracle.v1.oracle_pb2.Request] = ...,
        reports : typing.Optional[typing.Iterable[oracle.v1.oracle_pb2.Report]] = ...,
        result : typing.Optional[oracle.v1.oracle_pb2.Result] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"request",b"request",u"result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"reports",b"reports",u"request",b"request",u"result",b"result"]) -> None: ...
global___QueryRequestResponse = QueryRequestResponse

# QueryPendingRequestRequest is request type for the Query/PendingRequests RPC
# method.
class QueryPendingRequestsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    # ValidatorAddress is address of a validator
    validator_address: typing.Text = ...
    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validator_address",b"validator_address"]) -> None: ...
global___QueryPendingRequestsRequest = QueryPendingRequestsRequest

# QueryPendingRequestResponse is response type for the Query/PendingRequests
# RPC method.
class QueryPendingRequestsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REQUEST_IDS_FIELD_NUMBER: builtins.int
    # RequestIDs is a list of pending request IDs assigned to the given validator
    @property
    def request_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        request_ids : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"request_ids",b"request_ids"]) -> None: ...
global___QueryPendingRequestsResponse = QueryPendingRequestsResponse

# QueryParamsRequest is request type for the Query/Params RPC method.
class QueryParamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___QueryParamsRequest = QueryParamsRequest

# QueryParamsResponse is response type for the Query/Params RPC method.
class QueryParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARAMS_FIELD_NUMBER: builtins.int
    # pagination defines an optional pagination for the request.
    @property
    def params(self) -> oracle.v1.oracle_pb2.Params: ...
    def __init__(self,
        *,
        params : typing.Optional[oracle.v1.oracle_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> None: ...
global___QueryParamsResponse = QueryParamsResponse

# QueryValidatorRequest is request type for the Query/Validator RPC method.
class QueryValidatorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    # ValidatorAddress is address of a validator
    validator_address: typing.Text = ...
    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validator_address",b"validator_address"]) -> None: ...
global___QueryValidatorRequest = QueryValidatorRequest

# QueryValidatorResponse is response type for the Query/Validator RPC method.
class QueryValidatorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    # Status is status of a validator e.g. active/inactive
    @property
    def status(self) -> oracle.v1.oracle_pb2.ValidatorStatus: ...
    def __init__(self,
        *,
        status : typing.Optional[oracle.v1.oracle_pb2.ValidatorStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> None: ...
global___QueryValidatorResponse = QueryValidatorResponse

# QueryIsReporterRequest is request type for the Query/Reporter RPC method.
class QueryIsReporterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    REPORTER_ADDRESS_FIELD_NUMBER: builtins.int
    # ValidatorAddress is a validator address
    validator_address: typing.Text = ...
    # ReporterAddress is a candidate account
    reporter_address: typing.Text = ...
    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        reporter_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"reporter_address",b"reporter_address",u"validator_address",b"validator_address"]) -> None: ...
global___QueryIsReporterRequest = QueryIsReporterRequest

# QueryIsReporterResponse is response type for the Query/Reporter RPC method.
class QueryIsReporterResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IS_REPORTER_FIELD_NUMBER: builtins.int
    # IsReporter is true if this account has been granted by validator
    is_reporter: builtins.bool = ...
    def __init__(self,
        *,
        is_reporter : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"is_reporter",b"is_reporter"]) -> None: ...
global___QueryIsReporterResponse = QueryIsReporterResponse

# QueryReportersRequest is request type for the Query/Reporters RPC method.
class QueryReportersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    # ValidatorAddress is a validator address
    validator_address: typing.Text = ...
    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validator_address",b"validator_address"]) -> None: ...
global___QueryReportersRequest = QueryReportersRequest

# QueryReportersResponse is response type for the Query/Reporters RPC method.
class QueryReportersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REPORTER_FIELD_NUMBER: builtins.int
    # Reporter is a list of account addresses of reporters
    @property
    def reporter(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        reporter : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"reporter",b"reporter"]) -> None: ...
global___QueryReportersResponse = QueryReportersResponse

# QueryActiveValidatorsRequest is request type for the Query/ActiveValidators
# RPC method.
class QueryActiveValidatorsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___QueryActiveValidatorsRequest = QueryActiveValidatorsRequest

# QueryActiveValidatorsResponse is response type for the Query/ActiveValidators
# RPC method.
class QueryActiveValidatorsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATORS_FIELD_NUMBER: builtins.int
    # Validators is a list of active validators
    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[oracle.v1.oracle_pb2.ActiveValidator]: ...
    def __init__(self,
        *,
        validators : typing.Optional[typing.Iterable[oracle.v1.oracle_pb2.ActiveValidator]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"validators",b"validators"]) -> None: ...
global___QueryActiveValidatorsResponse = QueryActiveValidatorsResponse

# QueryRequestSearchRequest is request type for the Query/RequestSearch RPC
# method.
class QueryRequestSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ORACLE_SCRIPT_ID_FIELD_NUMBER: builtins.int
    CALLDATA_FIELD_NUMBER: builtins.int
    ASK_COUNT_FIELD_NUMBER: builtins.int
    MIN_COUNT_FIELD_NUMBER: builtins.int
    # OracleScriptID is ID of an oracle script
    oracle_script_id: builtins.int = ...
    # Calldata is OBI-encoded data in hex format as argument params for the
    # oracle script
    calldata: typing.Text = ...
    # AskCount is number of validators allowed for fulfilling the request
    ask_count: builtins.int = ...
    # MinCount is number of validators required for fulfilling the request
    min_count: builtins.int = ...
    def __init__(self,
        *,
        oracle_script_id : builtins.int = ...,
        calldata : typing.Text = ...,
        ask_count : builtins.int = ...,
        min_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"ask_count",b"ask_count",u"calldata",b"calldata",u"min_count",b"min_count",u"oracle_script_id",b"oracle_script_id"]) -> None: ...
global___QueryRequestSearchRequest = QueryRequestSearchRequest

# QueryRequestSearchResponse is response type for the Query/RequestSearch RPC
# method.
class QueryRequestSearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REQUEST_FIELD_NUMBER: builtins.int
    # Request is details of an oracle request
    @property
    def request(self) -> global___QueryRequestResponse: ...
    def __init__(self,
        *,
        request : typing.Optional[global___QueryRequestResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"request",b"request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"request",b"request"]) -> None: ...
global___QueryRequestSearchResponse = QueryRequestSearchResponse

# QueryRequestPriceRequest is request type for the Query/RequestPrice RPC
# method.
class QueryRequestPriceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SYMBOLS_FIELD_NUMBER: builtins.int
    ASK_COUNT_FIELD_NUMBER: builtins.int
    MIN_COUNT_FIELD_NUMBER: builtins.int
    # Symbol is unit of data indicating what the data is
    @property
    def symbols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    # AskCount is number of validators allowed for fulfilling the request
    ask_count: builtins.int = ...
    # MinCount is number of validators required for fulfilling the request
    min_count: builtins.int = ...
    def __init__(self,
        *,
        symbols : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ask_count : builtins.int = ...,
        min_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"ask_count",b"ask_count",u"min_count",b"min_count",u"symbols",b"symbols"]) -> None: ...
global___QueryRequestPriceRequest = QueryRequestPriceRequest

# QueryRequestPriceResponse is response type for the Query/RequestPrice RPC
# method.
class QueryRequestPriceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PRICE_RESULTS_FIELD_NUMBER: builtins.int
    # PriceResult is a list of price results for given symbols
    @property
    def price_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[oracle.v1.oracle_pb2.PriceResult]: ...
    def __init__(self,
        *,
        price_results : typing.Optional[typing.Iterable[oracle.v1.oracle_pb2.PriceResult]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"price_results",b"price_results"]) -> None: ...
global___QueryRequestPriceResponse = QueryRequestPriceResponse

# QueryRequestVerificationRequest is request type for the
# Query/RequestVerification RPC
class QueryRequestVerificationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHAIN_ID_FIELD_NUMBER: builtins.int
    VALIDATOR_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    EXTERNAL_ID_FIELD_NUMBER: builtins.int
    REPORTER_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    # ChainID is the chain ID to identify which chain ID is used for the
    # verification
    chain_id: typing.Text = ...
    # Validator is a validator address
    validator: typing.Text = ...
    # RequestID is oracle request ID
    request_id: builtins.int = ...
    # ExternalID is an oracle's external ID
    external_id: builtins.int = ...
    # Reporter is an bech32-encoded public key of the reporter authorized by the
    # validator
    reporter: typing.Text = ...
    # Signature is a signature signed by the reporter using reporter's private
    # key
    signature: builtins.bytes = ...
    def __init__(self,
        *,
        chain_id : typing.Text = ...,
        validator : typing.Text = ...,
        request_id : builtins.int = ...,
        external_id : builtins.int = ...,
        reporter : typing.Text = ...,
        signature : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"chain_id",b"chain_id",u"external_id",b"external_id",u"reporter",b"reporter",u"request_id",b"request_id",u"signature",b"signature",u"validator",b"validator"]) -> None: ...
global___QueryRequestVerificationRequest = QueryRequestVerificationRequest

# QueryRequestVerificationResponse is response type for the
# Query/RequestVerification RPC
class QueryRequestVerificationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHAIN_ID_FIELD_NUMBER: builtins.int
    VALIDATOR_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    EXTERNAL_ID_FIELD_NUMBER: builtins.int
    DATA_SOURCE_ID_FIELD_NUMBER: builtins.int
    # ChainID is the targeted chain ID
    chain_id: typing.Text = ...
    # Validator is the targeted validator address
    validator: typing.Text = ...
    # RequestID is the ID of targeted request
    request_id: builtins.int = ...
    # ExternalID is the ID of targeted oracle's external data source
    external_id: builtins.int = ...
    # DataSourceID is the ID of a data source that relates to the targeted
    # external ID
    data_source_id: builtins.int = ...
    def __init__(self,
        *,
        chain_id : typing.Text = ...,
        validator : typing.Text = ...,
        request_id : builtins.int = ...,
        external_id : builtins.int = ...,
        data_source_id : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"chain_id",b"chain_id",u"data_source_id",b"data_source_id",u"external_id",b"external_id",u"request_id",b"request_id",u"validator",b"validator"]) -> None: ...
global___QueryRequestVerificationResponse = QueryRequestVerificationResponse
