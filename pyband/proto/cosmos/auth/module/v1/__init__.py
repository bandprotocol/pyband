# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/auth/module/v1beta1/module.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class Module(betterproto.Message):
    """Module is the config object for the auth module."""

    bech32_prefix: str = betterproto.string_field(1)
    """bech32_prefix is the bech32 account prefix for the app."""

    module_account_permissions: List["ModuleAccountPermission"] = (
        betterproto.message_field(2)
    )
    """module_account_permissions are module account permissions."""

    authority: str = betterproto.string_field(3)
    """
    authority defines the custom module authority. If not set, defaults to the governance module.
    """


@dataclass(eq=False, repr=False)
class ModuleAccountPermission(betterproto.Message):
    """ModuleAccountPermission represents permissions for a module account."""

    account: str = betterproto.string_field(1)
    """account is the name of the module."""

    permissions: List[str] = betterproto.string_field(2)
    """
    permissions are the permissions this module has. Currently recognized
     values are minter, burner and staking.
    """
