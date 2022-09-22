from dataclasses import dataclass

from ....common import MessageWrapper
from .....proto.cosmos.bank.v1beta1 import MsgMultiSend as MsgMultiSendProto
from .....proto.cosmos.bank.v1beta1 import MsgSend as MsgSendProto

try:
    from .....proto.cosmos.base import v1beta1 as __base_v1_beta1__
    from .....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__
except ImportError as ie:
    raise ie


@dataclass
class MsgSend(MessageWrapper, MsgSendProto):
    @property
    def type_url(self):
        return "/cosmos.bank.v1beta1.MsgSend"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgSend"


@dataclass
class MsgMultiSend(MessageWrapper, MsgMultiSendProto):
    @property
    def type_url(self):
        return "/cosmos.bank.v1beta1.MsgMultiSend"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgMultiSend"
