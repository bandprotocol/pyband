from dataclasses import dataclass

from ....base import BaseMessageWrapper
from .....proto.cosmos.bank.v1beta1 import MsgMultiSend as MsgMultiSendProto
from .....proto.cosmos.bank.v1beta1 import MsgSend as MsgSendProto
from .....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from .....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__

assert __base_v1_beta1__
assert __base_query_v1_beta1__


class MsgSend(BaseMessageWrapper, MsgSendProto):
    @property
    def type_url(self):
        return "/cosmos.bank.v1beta1.MsgSend"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgSend"


class MsgMultiSend(BaseMessageWrapper, MsgMultiSendProto):
    @property
    def type_url(self):
        return "/cosmos.bank.v1beta1.MsgMultiSend"

    @property
    def legacy_url(self):
        return "cosmos-sdk/MsgMultiSend"
