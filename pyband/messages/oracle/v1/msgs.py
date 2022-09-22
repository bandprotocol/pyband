from dataclasses import dataclass

from ....messages.common import MessageWrapper
from ....proto.oracle.v1 import MsgCreateDataSource as MsgCreateDataSourceProto
from ....proto.oracle.v1 import MsgCreateDataSource as MsgRequestDataProto
from ....proto.oracle.v1 import MsgCreateOracleScript as MsgCreateOracleScriptProto
from ....proto.oracle.v1 import MsgEditDataSource as MsgEditDataSourceProto
from ....proto.oracle.v1 import MsgEditOracleScript as MsgEditOracleScriptProto

try:
    from ....proto.cosmos.base import v1beta1 as __cosmos_base_v1_beta1__
except ImportError as ie:
    raise ie


class MsgRequestData(MessageWrapper, MsgRequestDataProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgRequestData"

    @property
    def legacy_url(self):
        return "oracle/Request"


@dataclass
class MsgCreateDataSource(MessageWrapper, MsgCreateDataSourceProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgCreateDataSource"

    @property
    def legacy_url(self):
        return "oracle/CreateDataSource"


class MsgEditDataSource(MessageWrapper, MsgEditDataSourceProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgEditDataSource"

    @property
    def legacy_url(self):
        return "oracle/EditDataSource"


class MsgCreateOracleScript(MessageWrapper, MsgCreateOracleScriptProto):
    @property
    def legacy_url(self):
        return "/oracle.v1.MsgCreateOracleScript"

    @property
    def type_url(self):
        return "oracle/CreateOracleScript"


class MsgEditOracleScript(MessageWrapper, MsgEditOracleScriptProto):
    @property
    def legacy_url(self):
        return "/oracle.v1.MsgEditOracleScript"

    @property
    def type_url(self):
        return "oracle/EditOracleScript"
