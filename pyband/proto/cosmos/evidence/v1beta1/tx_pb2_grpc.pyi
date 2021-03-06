"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .tx_pb2 import *
# Msg defines the evidence Msg service.
class MsgStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # SubmitEvidence submits an arbitrary Evidence of misbehavior such as equivocation or
    # counterfactual signing.
    SubmitEvidence:grpc.UnaryUnaryMultiCallable[
        global___MsgSubmitEvidence,
        global___MsgSubmitEvidenceResponse] = ...


# Msg defines the evidence Msg service.
class MsgServicer(metaclass=abc.ABCMeta):
    # SubmitEvidence submits an arbitrary Evidence of misbehavior such as equivocation or
    # counterfactual signing.
    @abc.abstractmethod
    def SubmitEvidence(self,
        request: global___MsgSubmitEvidence,
        context: grpc.ServicerContext,
    ) -> global___MsgSubmitEvidenceResponse: ...


def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
