"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.gov.v1beta1.gov_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STARTING_PROPOSAL_ID_FIELD_NUMBER: builtins.int
    DEPOSITS_FIELD_NUMBER: builtins.int
    VOTES_FIELD_NUMBER: builtins.int
    PROPOSALS_FIELD_NUMBER: builtins.int
    DEPOSIT_PARAMS_FIELD_NUMBER: builtins.int
    VOTING_PARAMS_FIELD_NUMBER: builtins.int
    TALLY_PARAMS_FIELD_NUMBER: builtins.int
    starting_proposal_id: builtins.int = ...

    @property
    def deposits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Deposit]: ...

    @property
    def votes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Vote]: ...

    @property
    def proposals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.gov.v1beta1.gov_pb2.Proposal]: ...

    @property
    def deposit_params(self) -> cosmos.gov.v1beta1.gov_pb2.DepositParams: ...

    @property
    def voting_params(self) -> cosmos.gov.v1beta1.gov_pb2.VotingParams: ...

    @property
    def tally_params(self) -> cosmos.gov.v1beta1.gov_pb2.TallyParams: ...

    def __init__(self,
        *,
        starting_proposal_id : builtins.int = ...,
        deposits : typing.Optional[typing.Iterable[cosmos.gov.v1beta1.gov_pb2.Deposit]] = ...,
        votes : typing.Optional[typing.Iterable[cosmos.gov.v1beta1.gov_pb2.Vote]] = ...,
        proposals : typing.Optional[typing.Iterable[cosmos.gov.v1beta1.gov_pb2.Proposal]] = ...,
        deposit_params : typing.Optional[cosmos.gov.v1beta1.gov_pb2.DepositParams] = ...,
        voting_params : typing.Optional[cosmos.gov.v1beta1.gov_pb2.VotingParams] = ...,
        tally_params : typing.Optional[cosmos.gov.v1beta1.gov_pb2.TallyParams] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"deposit_params",b"deposit_params",u"tally_params",b"tally_params",u"voting_params",b"voting_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"deposit_params",b"deposit_params",u"deposits",b"deposits",u"proposals",b"proposals",u"starting_proposal_id",b"starting_proposal_id",u"tally_params",b"tally_params",u"votes",b"votes",u"voting_params",b"voting_params"]) -> None: ...
global___GenesisState = GenesisState