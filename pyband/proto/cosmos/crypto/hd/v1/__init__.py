# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/crypto/hd/v1beta1/hd.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class Bip44Params(betterproto.Message):
    """BIP44Params is used as path field in ledger item in Record."""

    purpose: int = betterproto.uint32_field(1)
    """
    purpose is a constant set to 44' (or 0x8000002C) following the BIP43 recommendation
    """

    coin_type: int = betterproto.uint32_field(2)
    """coin_type is a constant that improves privacy"""

    account: int = betterproto.uint32_field(3)
    """account splits the key space into independent user identities"""

    change: bool = betterproto.bool_field(4)
    """
    change is a constant used for public derivation. Constant 0 is used for external chain and constant 1 for internal
     chain.
    """

    address_index: int = betterproto.uint32_field(5)
    """address_index is used as child index in BIP32 derivation"""
