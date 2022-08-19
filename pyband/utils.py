import re
import json

from typing import List
from google.protobuf.any_pb2 import Any as AnyProtobuf
from .exceptions import NotBip44Error, IncorrectLengthError
from google.protobuf.json_format import MessageToJson


def is_bip44(derivation_path: str) -> bool:
    if re.search("^m(/[0-9]+['hH]?)*$", derivation_path) is not None:
        return True
    else:
        return False


def bip44_to_list(derivation_path: str) -> List[int]:
    try:
        return [int(x) for x in derivation_path.replace("'", "").split("/")[1:]]
    except ValueError:
        raise NotBip44Error
    except Exception as e:
        raise e


def get_bip32_byte(derivation_path: List[int], harden_count: int) -> bytes:
    if len(derivation_path) != 5:
        raise IncorrectLengthError("Incorrect path length")

    path_bytes = b""
    for i, idx in enumerate(derivation_path):
        if i < harden_count:
            idx = 0x80000000 | idx
        path_bytes += idx.to_bytes(4, "little")
    return path_bytes


def split_packet(byte_message: bytes) -> List[bytes]:
    return [bytes(byte_message[i : i + 250]) for i in range(0, len(byte_message), 250)]


def protobuf_to_json(protobuf: AnyProtobuf):
    res: dict = json.loads(MessageToJson(protobuf))
    msg_type = res["@type"].split(".")
    new_msg_type = "{x}/{y}".format(x=msg_type[0][1:].replace("cosmos", "cosmos-sdk"), y=msg_type[-1])
    res.pop("@type")
    val = {re.sub(r"(?<!^)(?=[A-Z])", "_", a).lower(): b for a, b in res.items()}
    return {"type": new_msg_type, "value": val}
