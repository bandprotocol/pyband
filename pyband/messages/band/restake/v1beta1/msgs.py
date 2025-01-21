from pyband.messages.base import BaseMessageWrapper
from pyband.proto.band.restake.v1beta1 import (
    MsgStake as MsgStakeProto,
    MsgUnstake as MsgUnstakeProto,
    MsgUpdateParams as MsgUpdateParamsProto,
)


class MsgStake(BaseMessageWrapper, MsgStakeProto):
    @property
    def type_url(self):
        return "/band.restake.v1beta1.MsgStake"

    @property
    def legacy_url(self):
        return "restake/MsgStake"


class MsgUnstake(BaseMessageWrapper, MsgUnstakeProto):
    @property
    def type_url(self):
        return "/band.restake.v1beta1.MsgUnstake"

    @property
    def legacy_url(self):
        return "restake/MsgUnstake"


class MsgUpdateParams(BaseMessageWrapper, MsgUpdateParamsProto):
    @property
    def type_url(self):
        return "/band.restake.v1beta1.MsgUpdateParams"

    @property
    def legacy_url(self):
        return "restake/MsgUpdateParams"
