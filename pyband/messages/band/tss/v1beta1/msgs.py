from pyband.messages.base import BaseMessageWrapper
from pyband.proto.band.tss.v1beta1 import (
    MsgSubmitDkgRound1 as MsgSubmitDkgRound1Proto,
    MsgSubmitDkgRound2 as MsgSubmitDkgRound2Proto,
    MsgComplain as MsgComplainProto,
    MsgConfirm as MsgConfirmProto,
    MsgSubmitDEs as MsgSubmitDEsProto,
    MsgResetDE as MsgResetDEProto,
    MsgSubmitSignature as MsgSubmitSignatureProto,
    MsgUpdateParams as MsgUpdateParamsProto,
)


class MsgSubmitDkgRound1(BaseMessageWrapper, MsgSubmitDkgRound1Proto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgSubmitDkgRound1"

    @property
    def legacy_url(self):
        return "tss/MsgSubmitDkgRound1"


class MsgSubmitDkgRound2(BaseMessageWrapper, MsgSubmitDkgRound2Proto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgSubmitDkgRound2"

    @property
    def legacy_url(self):
        return "tss/MsgSubmitDkgRound2"


class MsgComplain(BaseMessageWrapper, MsgComplainProto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgComplaint"

    @property
    def legacy_url(self):
        return "tss/MsgComplaint"


class MsgConfirm(BaseMessageWrapper, MsgConfirmProto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgConfirm"

    @property
    def legacy_url(self):
        return "tss/MsgConfirm"


class MsgSubmitDEs(BaseMessageWrapper, MsgSubmitDEsProto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgSubmitDEs"

    @property
    def legacy_url(self):
        return "tss/MsgSubmitDEs"


class MsgResetDE(BaseMessageWrapper, MsgResetDEProto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgResetDE"

    @property
    def legacy_url(self):
        return "tss/MsgResetDE"


class MsgSubmitSignature(BaseMessageWrapper, MsgSubmitSignatureProto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgSubmitSignature"

    @property
    def legacy_url(self):
        return "tss/MsgSubmitSignature"


class MsgUpdateParams(BaseMessageWrapper, MsgUpdateParamsProto):
    @property
    def type_url(self):
        return "/band.tss.v1beta1.MsgUpdateParams"

    @property
    def legacy_url(self):
        return "tss/MsgUpdateParams"
