# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/group/module/v1beta1/module.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from datetime import timedelta

import betterproto


@dataclass(eq=False, repr=False)
class Module(betterproto.Message):
    """Module is the config object of the group module."""

    max_execution_period: timedelta = betterproto.message_field(1)
    """
    max_execution_period defines the max duration after a proposal's voting period ends that members can send a MsgExec
     to execute the proposal.
    """

    max_metadata_len: int = betterproto.uint64_field(2)
    """
    max_metadata_len defines the max length of the metadata bytes field for various entities within the group module.
     Defaults to 255 if not explicitly set.
    """
