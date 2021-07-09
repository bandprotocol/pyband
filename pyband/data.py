import base64

from dataclasses import dataclass
from typing import List, Optional, NewType
from dacite import Config
from .utils import parse_epoch_time
from .wallet import Address
from .exceptions import NegativeIntegerError

HexBytes = NewType("HexBytes", bytes)
EpochTime = NewType("EpochTime", int)


@dataclass
class RawRequest(object):
    data_source_id: int
    external_id: int = 0
    calldata: bytes = b""


@dataclass
class IBCChannel(object):
    port_id: str
    channel_id: str


@dataclass
class Request(object):
    oracle_script_id: int
    requested_validators: List[str]
    min_count: int
    request_height: int
    raw_requests: List[RawRequest]
    execute_gas: int
    ibc_channel: Optional[IBCChannel]
    client_id: str = ""
    calldata: bytes = b""


@dataclass
class RawReport(object):
    exit_code: int
    data: Optional[bytes]
    external_id: int = 0


@dataclass
class Report(object):
    validator: str
    raw_reports: List[RawReport]
    in_before_resolve: bool = False


@dataclass
class Result(object):
    oracle_script_id: int
    ask_count: int
    min_count: int
    request_time: int
    resolve_time: int
    resolve_status: str
    request_id: int
    ans_count: int
    result: Optional[bytes]
    client_id: str = ""
    calldata: bytes = b""


@dataclass
class RequestInfo(object):
    request: Optional[Request]
    reports: Optional[List[Report]]
    result: Optional[Result]


@dataclass
class Account(object):
    address: Address
    pub_key: Optional[dict]
    account_number: int
    sequence: int


@dataclass
class BlockHeaderInfo(object):
    chain_id: str
    height: int
    time: EpochTime
    last_commit_hash: HexBytes
    data_hash: HexBytes
    validators_hash: HexBytes
    next_validators_hash: HexBytes
    consensus_hash: HexBytes
    app_hash: HexBytes
    last_results_hash: HexBytes
    evidence_hash: HexBytes
    proposer_address: HexBytes


@dataclass
class BlockHeader(object):
    header: BlockHeaderInfo


@dataclass
class BlockID(object):
    hash: HexBytes


@dataclass
class Block(object):
    block: BlockHeader
    block_id: BlockID


@dataclass
class ReferencePriceUpdated(object):
    base: int
    quote: int


@dataclass
class ReferencePrice(object):
    pair: str
    rate: float
    updated_at: ReferencePriceUpdated


@dataclass
class EVMProof(object):
    json_proof: dict
    evm_proof_bytes: HexBytes
