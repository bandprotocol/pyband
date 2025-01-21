from pyband.messages.base import BaseMessageWrapper
from pyband.proto.band.globalfee.v1beta1 import (
    MsgUpdateParams as MsgUpdateParamsProto,
)


class MsgUpdateParams(BaseMessageWrapper, MsgUpdateParamsProto):
    @property
    def type_url(self):
        return "/band.globalfee.v1beta1.MsgUpdateParams"

    @property
    def legacy_url(self):
        return "globalfee/MsgUpdateParams"
