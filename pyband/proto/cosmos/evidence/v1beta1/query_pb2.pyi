"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class QueryEvidenceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EVIDENCE_HASH_FIELD_NUMBER: builtins.int
    evidence_hash: builtins.bytes = ...

    def __init__(self,
        *,
        evidence_hash : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"evidence_hash",b"evidence_hash"]) -> None: ...
global___QueryEvidenceRequest = QueryEvidenceRequest

class QueryEvidenceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EVIDENCE_FIELD_NUMBER: builtins.int

    @property
    def evidence(self) -> google.protobuf.any_pb2.Any: ...

    def __init__(self,
        *,
        evidence : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"evidence",b"evidence"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"evidence",b"evidence"]) -> None: ...
global___QueryEvidenceResponse = QueryEvidenceResponse

class QueryAllEvidenceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> None: ...
global___QueryAllEvidenceRequest = QueryAllEvidenceRequest

class QueryAllEvidenceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EVIDENCE_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def evidence(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        evidence : typing.Optional[typing.Iterable[google.protobuf.any_pb2.Any]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"evidence",b"evidence",u"pagination",b"pagination"]) -> None: ...
global___QueryAllEvidenceResponse = QueryAllEvidenceResponse