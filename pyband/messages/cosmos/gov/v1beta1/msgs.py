from dataclasses import dataclass

from ....common import MessageWrapper
from .....proto.cosmos.gov.v1beta1 import MsgVote as MsgVoteProto

try:
    from .....proto.cosmos.base import v1beta1 as __base_v1_beta1__
    from .....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__
except ImportError as ie:
    raise ie


@dataclass
class MsgVote(MessageWrapper, MsgVoteProto):
    @property
    def type_url(self):
        return "/cosmos.gov.v1beta1.MsgVote"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgVote"
