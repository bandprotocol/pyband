from pyband.messages.base import BaseMessageWrapper
from pyband.proto.band.feeds.v1beta1 import (
    MsgVote as MsgVoteProto,
    MsgSubmitSignalPrices as MsgSubmitSignalPricesProto,
    MsgUpdateReferenceSourceConfig as MsgUpdateReferenceSourceConfigProto,
    MsgUpdateParams as MsgUpdateParamsProto,
)


class MsgVote(BaseMessageWrapper, MsgVoteProto):
    @property
    def type_url(self):
        return "/band.feeds.v1beta1.MsgVote"

    @property
    def legacy_url(self):
        return "feeds/MsgVote"


class MsgSubmitSignalPrices(BaseMessageWrapper, MsgSubmitSignalPricesProto):
    @property
    def type_url(self):
        return "/band.feeds.v1beta1.MsgSubmitSignalPrices"

    @property
    def legacy_url(self):
        return "feeds/MsgSubmitSignalPrices"


class MsgUpdateReferenceSourceConfig(
    BaseMessageWrapper, MsgUpdateReferenceSourceConfigProto
):
    @property
    def type_url(self):
        return "/band.feeds.v1beta1.MsgUpdateReferenceSourceConfig"

    @property
    def legacy_url(self):
        return "feeds/MsgUpdateReferenceSourceConfig"


class MsgUpdateParams(BaseMessageWrapper, MsgUpdateParamsProto):
    @property
    def type_url(self):
        return "/band.feeds.v1beta1.MsgUpdateParams"

    @property
    def legacy_url(self):
        return "feeds/MsgUpdateParams"
