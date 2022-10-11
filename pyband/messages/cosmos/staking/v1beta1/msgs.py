from dataclasses import dataclass

from ....base import BaseMessageWrapper
from .....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from .....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__
from .....proto.cosmos.staking.v1beta1 import MsgBeginRedelegate as MsgBeginRedelegateProto
from .....proto.cosmos.staking.v1beta1 import MsgDelegate as MsgDelegateProto
from .....proto.cosmos.staking.v1beta1 import MsgUndelegate as MsgUndelegateProto
from .....proto.tendermint import types as ___tendermint_types__

assert __base_v1_beta1__
assert __base_query_v1_beta1__
assert ___tendermint_types__


class MsgBeginRedelegate(BaseMessageWrapper, MsgBeginRedelegateProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgBeginRedelegate"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgBeginRedelegate"


class MsgDelegate(BaseMessageWrapper, MsgDelegateProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgDelegate"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgDelegate"


class MsgUndelegate(BaseMessageWrapper, MsgUndelegateProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgUndelegate"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgUndelegate"
