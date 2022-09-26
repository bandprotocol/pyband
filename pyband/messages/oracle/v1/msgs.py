from dataclasses import dataclass

from ....messages.base import BaseMessageWrapper
from ....proto.cosmos.base import v1beta1 as __cosmos_base_v1_beta1__
from ....proto.oracle.v1 import MsgCreateDataSource as MsgCreateDataSourceProto
from ....proto.oracle.v1 import MsgCreateDataSource as MsgRequestDataProto
from ....proto.oracle.v1 import MsgCreateOracleScript as MsgCreateOracleScriptProto
from ....proto.oracle.v1 import MsgEditDataSource as MsgEditDataSourceProto
from ....proto.oracle.v1 import MsgEditOracleScript as MsgEditOracleScriptProto

assert __cosmos_base_v1_beta1__


class MsgRequestData(BaseMessageWrapper, MsgRequestDataProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgRequestData"

    @property
    def legacy_url(self):
        return "oracle/Request"


@dataclass
class MsgCreateDataSource(BaseMessageWrapper, MsgCreateDataSourceProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgCreateDataSource"

    @property
    def legacy_url(self):
        return "oracle/CreateDataSource"


class MsgEditDataSource(BaseMessageWrapper, MsgEditDataSourceProto):
    @property
    def type_url(self):
        return "/oracle.v1.MsgEditDataSource"

    @property
    def legacy_url(self):
        return "oracle/EditDataSource"


class MsgCreateOracleScript(BaseMessageWrapper, MsgCreateOracleScriptProto):
    @property
    def legacy_url(self):
        return "/oracle.v1.MsgCreateOracleScript"

    @property
    def type_url(self):
        return "oracle/CreateOracleScript"


class MsgEditOracleScript(BaseMessageWrapper, MsgEditOracleScriptProto):
    @property
    def legacy_url(self):
        return "/oracle.v1.MsgEditOracleScript"

    @property
    def type_url(self):
        return "oracle/EditOracleScript"
