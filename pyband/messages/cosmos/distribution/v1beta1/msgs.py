from dataclasses import dataclass

from ....base import BaseMessageWrapper
from .....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from .....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__
from .....proto.cosmos.distribution.v1beta1 import MsgWithdrawDelegatorReward as MsgWithdrawDelegatorRewardProto

assert __base_v1_beta1__
assert __base_query_v1_beta1__


class MsgWithdrawDelegationReward(BaseMessageWrapper, MsgWithdrawDelegatorRewardProto):
    @property
    def type_url(self):
        return "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgWithdrawDelegationReward"
