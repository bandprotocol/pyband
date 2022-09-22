from typing import List
from dataclasses import dataclass

from ....messages.common import MessageWrapper
from ....proto.oracle.v1 import MsgActivate as MsgActivateProto
from ....proto.oracle.v1 import MsgCreateDataSource as MsgCreateDataSourceProto
from ....proto.oracle.v1 import MsgCreateDataSource as MsgRequestDataProto
from ....proto.oracle.v1 import MsgCreateOracleScript as MsgCreateOracleScriptProto
from ....proto.oracle.v1 import MsgEditDataSource as MsgEditDataSourceProto
from ....proto.oracle.v1 import MsgEditOracleScript as MsgEditOracleScriptProto
from ....proto.oracle.v1 import MsgReportData as MsgReportDataProto

try:
    from ....proto.cosmos.base import v1beta1 as __cosmos_base_v1_beta1__
except ImportError as ie:
    raise ie


class MsgReportData(MessageWrapper, MsgReportDataProto):
    @property
    def type_url(self):
        return "oracle/MsgReportData"

    @property
    def legacy_url(self):
        return "/oracle.v1.MsgReportData"


class MsgRequestData(MessageWrapper, MsgRequestDataProto):
    @property
    def type_url(self):
        return "oracle/MsgRequestData"

    @property
    def legacy_url(self):
        return "/oracle.v1.MsgRequestData"


@dataclass
class MsgCreateDataSource(MessageWrapper, MsgCreateDataSourceProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgCreateDataSource"

    @property
    def legacy_url(self):
        return "oracle/MsgCreateDataSource"


class MsgEditDataSource(MessageWrapper, MsgEditDataSourceProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgEditDataSource"

    @property
    def legacy_url(self):
        return "oracle/MsgEditDataSource"


class MsgCreateOracleScript(MessageWrapper, MsgCreateOracleScriptProto):
    @property
    def legacy_url(self):
        return "/oracle.v1.MsgCreateOracleScript"

    @property
    def type_url(self):
        return "oracle/MsgCreateOracleScript"


class MsgEditOracleScript(MessageWrapper, MsgEditOracleScriptProto):
    @property
    def legacy_url(self):
        return "/oracle.v1.MsgEditOracleScript"

    @property
    def type_url(self):
        return "oracle/MsgEditOracleScript"


class MsgActivate(MessageWrapper, MsgActivateProto):
    @property
    def legacy_url(self):
        return "/oracle.v1.MsgActivate"

    @property
    def type_url(self):
        return "oracle/MsgActivate"
