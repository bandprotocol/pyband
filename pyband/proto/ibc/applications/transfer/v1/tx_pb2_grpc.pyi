"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .tx_pb2 import *
# Msg defines the ibc/transfer Msg service.
class MsgStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # Transfer defines a rpc handler method for MsgTransfer.
    Transfer:grpc.UnaryUnaryMultiCallable[
        global___MsgTransfer,
        global___MsgTransferResponse] = ...


# Msg defines the ibc/transfer Msg service.
class MsgServicer(metaclass=abc.ABCMeta):
    # Transfer defines a rpc handler method for MsgTransfer.
    @abc.abstractmethod
    def Transfer(self,
        request: global___MsgTransfer,
        context: grpc.ServicerContext,
    ) -> global___MsgTransferResponse: ...


def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
