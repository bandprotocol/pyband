from pyband.messages.base import BaseMessageWrapper
from pyband.proto.band.tunnel.v1beta1 import (
    MsgCreateTunnel as MsgCreateTunnelProto,
    MsgUpdateRoute as MsgUpdateRouteProto,
    MsgUpdateSignalsAndInterval as MsgUpdateSignalsAndIntervalProto,
    MsgActivate as MsgActivateProto,
    MsgDeactivate as MsgDeactivateProto,
    MsgTriggerTunnel as MsgTriggerTunnelProto,
    MsgDepositToTunnel as MsgDepositToTunnelProto,
    MsgWithdrawFromTunnel as MsgWithdrawFromTunnelProto,
)


class MsgCreateTunnel(BaseMessageWrapper, MsgCreateTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgCreateTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgCreateTunnel"


class MsgUpdateRoute(BaseMessageWrapper, MsgUpdateRouteProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgUpdateRoute"

    @property
    def legacy_url(self):
        return "tunnel/MsgUpdateRoute"


class MsgUpdateSignalsAndInterval(BaseMessageWrapper, MsgUpdateSignalsAndIntervalProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgUpdateSignalsAndInterval"

    @property
    def legacy_url(self):
        return "tunnel/MsgUpdateSignalsAndInterval"


class MsgActivate(BaseMessageWrapper, MsgActivateProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgActivate"

    @property
    def legacy_url(self):
        return "tunnel/MsgActivate"


class MsgDeactivate(BaseMessageWrapper, MsgDeactivateProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgDeactivate"

    @property
    def legacy_url(self):
        return "tunnel/MsgDeactivate"


class MsgTriggerTunnel(BaseMessageWrapper, MsgTriggerTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgTriggerTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgTriggerTunnel"


class MsgDepositToTunnel(BaseMessageWrapper, MsgDepositToTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgDepositToTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgDepositToTunnel"


class MsgWithdrawFromTunnel(BaseMessageWrapper, MsgWithdrawFromTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1beta1.MsgWithdrawFromTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgWithdrawFromTunnel"
