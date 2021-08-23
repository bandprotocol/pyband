"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .query_pb2 import *
class QueryStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Proposal:grpc.UnaryUnaryMultiCallable[
        global___QueryProposalRequest,
        global___QueryProposalResponse] = ...

    Proposals:grpc.UnaryUnaryMultiCallable[
        global___QueryProposalsRequest,
        global___QueryProposalsResponse] = ...

    Vote:grpc.UnaryUnaryMultiCallable[
        global___QueryVoteRequest,
        global___QueryVoteResponse] = ...

    Votes:grpc.UnaryUnaryMultiCallable[
        global___QueryVotesRequest,
        global___QueryVotesResponse] = ...

    Params:grpc.UnaryUnaryMultiCallable[
        global___QueryParamsRequest,
        global___QueryParamsResponse] = ...

    Deposit:grpc.UnaryUnaryMultiCallable[
        global___QueryDepositRequest,
        global___QueryDepositResponse] = ...

    Deposits:grpc.UnaryUnaryMultiCallable[
        global___QueryDepositsRequest,
        global___QueryDepositsResponse] = ...

    TallyResult:grpc.UnaryUnaryMultiCallable[
        global___QueryTallyResultRequest,
        global___QueryTallyResultResponse] = ...


class QueryServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Proposal(self,
        request: global___QueryProposalRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryProposalResponse: ...

    @abc.abstractmethod
    def Proposals(self,
        request: global___QueryProposalsRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryProposalsResponse: ...

    @abc.abstractmethod
    def Vote(self,
        request: global___QueryVoteRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryVoteResponse: ...

    @abc.abstractmethod
    def Votes(self,
        request: global___QueryVotesRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryVotesResponse: ...

    @abc.abstractmethod
    def Params(self,
        request: global___QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryParamsResponse: ...

    @abc.abstractmethod
    def Deposit(self,
        request: global___QueryDepositRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryDepositResponse: ...

    @abc.abstractmethod
    def Deposits(self,
        request: global___QueryDepositsRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryDepositsResponse: ...

    @abc.abstractmethod
    def TallyResult(self,
        request: global___QueryTallyResultRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryTallyResultResponse: ...


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...