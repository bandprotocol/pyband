# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/base/snapshots/v1beta1/snapshot.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class Snapshot(betterproto.Message):
    """Snapshot contains Tendermint state sync snapshot info."""

    height: int = betterproto.uint64_field(1)
    format: int = betterproto.uint32_field(2)
    chunks: int = betterproto.uint32_field(3)
    hash: bytes = betterproto.bytes_field(4)
    metadata: "Metadata" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class Metadata(betterproto.Message):
    """Metadata contains SDK-specific snapshot metadata."""

    chunk_hashes: List[bytes] = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class SnapshotItem(betterproto.Message):
    """
    SnapshotItem is an item contained in a rootmulti.Store snapshot. Since:
    cosmos-sdk 0.46
    """

    store: "SnapshotStoreItem" = betterproto.message_field(1, group="item")
    iavl: "SnapshotIavlItem" = betterproto.message_field(2, group="item")
    extension: "SnapshotExtensionMeta" = betterproto.message_field(3, group="item")
    extension_payload: "SnapshotExtensionPayload" = betterproto.message_field(
        4, group="item"
    )
    kv: "SnapshotKvItem" = betterproto.message_field(5, group="item")
    schema: "SnapshotSchema" = betterproto.message_field(6, group="item")

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("kv"):
            warnings.warn("SnapshotItem.kv is deprecated", DeprecationWarning)
        if self.is_set("schema"):
            warnings.warn("SnapshotItem.schema is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class SnapshotStoreItem(betterproto.Message):
    """
    SnapshotStoreItem contains metadata about a snapshotted store. Since:
    cosmos-sdk 0.46
    """

    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SnapshotIavlItem(betterproto.Message):
    """SnapshotIAVLItem is an exported IAVL node. Since: cosmos-sdk 0.46"""

    key: bytes = betterproto.bytes_field(1)
    value: bytes = betterproto.bytes_field(2)
    version: int = betterproto.int64_field(3)
    """version is block height"""

    height: int = betterproto.int32_field(4)
    """height is depth of the tree."""


@dataclass(eq=False, repr=False)
class SnapshotExtensionMeta(betterproto.Message):
    """
    SnapshotExtensionMeta contains metadata about an external snapshotter.
    Since: cosmos-sdk 0.46
    """

    name: str = betterproto.string_field(1)
    format: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class SnapshotExtensionPayload(betterproto.Message):
    """
    SnapshotExtensionPayload contains payloads of an external snapshotter.
    Since: cosmos-sdk 0.46
    """

    payload: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class SnapshotKvItem(betterproto.Message):
    """
    SnapshotKVItem is an exported Key/Value Pair Since: cosmos-sdk 0.46
    Deprecated: This message was part of store/v2alpha1 which has been deleted
    from v0.47.
    """

    key: bytes = betterproto.bytes_field(1)
    value: bytes = betterproto.bytes_field(2)

    def __post_init__(self) -> None:
        warnings.warn("SnapshotKvItem is deprecated", DeprecationWarning)
        super().__post_init__()


@dataclass(eq=False, repr=False)
class SnapshotSchema(betterproto.Message):
    """
    SnapshotSchema is an exported schema of smt store Since: cosmos-sdk 0.46
    Deprecated: This message was part of store/v2alpha1 which has been deleted
    from v0.47.
    """

    keys: List[bytes] = betterproto.bytes_field(1)

    def __post_init__(self) -> None:
        warnings.warn("SnapshotSchema is deprecated", DeprecationWarning)
        super().__post_init__()
