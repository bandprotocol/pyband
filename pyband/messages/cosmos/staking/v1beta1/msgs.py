from dataclasses import dataclass

from ....common import MessageWrapper
from .....proto.cosmos.staking.v1beta1 import MsgBeginRedelegate as MsgBeginRedelegateProto
from .....proto.cosmos.staking.v1beta1 import MsgCreateValidator as MsgCreateValidatorProto
from .....proto.cosmos.staking.v1beta1 import MsgDelegate as MsgDelegateProto
from .....proto.cosmos.staking.v1beta1 import MsgEditValidator as MsgEditValidatorProto
from .....proto.cosmos.staking.v1beta1 import MsgUndelegate as MsgUndelegateProto

try:
    from .....proto.tendermint import types as ___tendermint_types__
    from .....proto.cosmos.base import v1beta1 as __base_v1_beta1__
    from .....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__
except ImportError as ie:
    raise ie


@dataclass
class MsgBeginRedelegate(MessageWrapper, MsgBeginRedelegateProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgBeginRedelegate"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgBeginRedelegate"


@dataclass
class MsgCreateValidator(MessageWrapper, MsgCreateValidatorProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgCreateValidator"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgCreateValidator"


@dataclass
class MsgDelegate(MessageWrapper, MsgDelegateProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgDelegate"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgDelegate"


@dataclass
class MsgUndelegate(MessageWrapper, MsgUndelegateProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgUndelegate"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgUndelegate"


@dataclass
class MsgEditValidator(MessageWrapper, MsgEditValidatorProto):
    @property
    def type_url(self):
        return "/cosmos.staking.v1beta1.MsgEditValidator"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgEditValidator"
