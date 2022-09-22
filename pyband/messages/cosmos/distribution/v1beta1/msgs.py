from dataclasses import dataclass

from ....common import MessageWrapper
from .....proto.cosmos.distribution.v1beta1 import MsgWithdrawDelegatorReward as MsgWithdrawDelegatorRewardProto

try:
    from .....proto.cosmos.base import v1beta1 as __base_v1_beta1__
    from .....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__
except ImportError as ie:
    raise ie


@dataclass
class MsgWithdrawDelegationReward(MessageWrapper, MsgWithdrawDelegatorRewardProto):
    @property
    def type_url(self):
        return "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgWithdrawDelegationReward"
