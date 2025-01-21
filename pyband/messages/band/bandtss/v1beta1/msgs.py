from pyband.messages.base import BaseMessageWrapper
from pyband.proto.band.bandtss.v1beta1 import (
    MsgRequestSignature as MsgRequestSignatureProto,
    MsgActivate as MsgActivateProto,
    MsgUpdateParams as MsgUpdateParamsProto,
    MsgTransitionGroup as MsgTransitionGroupProto,
    MsgForceTransitionGroup as MsgForceTransitionGroupProto,
)


class MsgRequestSignature(BaseMessageWrapper, MsgRequestSignatureProto):
    @property
    def type_url(self):
        return "/band.bandtss.v1beta1.MsgRequestData"

    @property
    def legacy_url(self):
        return "bandtss/MsgRequestSignature"


class MsgActivate(BaseMessageWrapper, MsgActivateProto):
    @property
    def type_url(self):
        return "/band.bandtss.v1beta1.MsgActivate"

    @property
    def legacy_url(self):
        return "bandtss/MsgActivate"


class MsgUpdateParams(BaseMessageWrapper, MsgUpdateParamsProto):
    @property
    def type_url(self):
        return "/band.bandtss.v1beta1.MsgUpdateParams"

    @property
    def legacy_url(self):
        return "bandtss/MsgUpdateParams"


class MsgTransitionGroup(BaseMessageWrapper, MsgTransitionGroupProto):
    @property
    def type_url(self):
        return "/band.bandtss.v1beta1.MsgTransitionGroup"

    @property
    def legacy_url(self):
        return "bandtss/MsgTransitionGroup"


class MsgForceTransitionGroup(BaseMessageWrapper, MsgForceTransitionGroupProto):
    @property
    def type_url(self):
        return "/band.bandtss.v1beta1.MsgForceTransitionGroup"

    @property
    def legacy_url(self):
        return "bandtss/MsgForceTransitionGroup"
