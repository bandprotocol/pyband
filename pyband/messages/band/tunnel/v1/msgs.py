from pyband.messages.base import BaseMessageWrapper
from pyband.proto.band.tunnel.v1beta1 import (
    MsgCreateTunnel as MsgCreateTunnelProto,
    MsgUpdateAndResetTunnel as MsgUpdateAndResetTunnelProto,
    MsgActivate as MsgActivateTunnelProto,
    MsgDeactivate as MsgDeactivateTunnelProto,
    MsgTriggerTunnel as MsgTriggerTunnelProto,
    MsgDepositToTunnel as MsgDepositToTunnelProto,
    MsgWithdrawFromTunnel as MsgWithdrawFromTunnelProto,
)


class MsgCreateTunnel(BaseMessageWrapper, MsgCreateTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1.MsgCreateTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgCreateTunnel"


class MsgUpdateAndResetTunnel(BaseMessageWrapper, MsgUpdateAndResetTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1.MsgUpdateAndResetTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgUpdateAndResetTunnel"


class MsgActivateTunnel(BaseMessageWrapper, MsgActivateTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1.MsgActivate"

    @property
    def legacy_url(self):
        return "tunnel/MsgActivate"


class MsgDeactivateTunnel(BaseMessageWrapper, MsgDeactivateTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1.MsgDeactivate"

    @property
    def legacy_url(self):
        return "tunnel/MsgDeactivate"


class MsgTriggerTunnel(BaseMessageWrapper, MsgTriggerTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1.MsgTriggerTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgTriggerTunnel"


class MsgDepositToTunnel(BaseMessageWrapper, MsgDepositToTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1.MsgDepositToTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgDepositToTunnel"


class MsgWithdrawFromTunnel(BaseMessageWrapper, MsgWithdrawFromTunnelProto):
    @property
    def type_url(self):
        return "/band.tunnel.v1.MsgWithdrawFromTunnel"

    @property
    def legacy_url(self):
        return "tunnel/MsgWithdrawFromTunnel"
