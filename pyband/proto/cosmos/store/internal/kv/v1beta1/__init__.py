# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/store/internal/kv/v1beta1/kv.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class Pairs(betterproto.Message):
    """Pairs defines a repeated slice of Pair objects."""

    pairs: List["Pair"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Pair(betterproto.Message):
    """Pair defines a key/value bytes tuple."""

    key: bytes = betterproto.bytes_field(1)
    value: bytes = betterproto.bytes_field(2)
