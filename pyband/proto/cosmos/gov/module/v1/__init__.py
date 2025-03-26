# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/gov/module/v1/module.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class Module(betterproto.Message):
    """Module is the config object of the gov module."""

    max_metadata_len: int = betterproto.uint64_field(1)
    """
    max_metadata_len defines the maximum proposal metadata length.
     Defaults to 255 if not explicitly set.
    """

    authority: str = betterproto.string_field(2)
    """
    authority defines the custom module authority. If not set, defaults to the governance module.
    """
