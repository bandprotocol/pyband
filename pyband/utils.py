import re

from typing import List, Dict
from google.protobuf.any_pb2 import Any as AnyProtobuf
from google.protobuf.json_format import MessageToDict
from .exceptions import NotBip44Error, IncorrectLengthError


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


def protobuf_to_json(protobuf: AnyProtobuf) -> Dict[str, str]:
    protobuf_as_dict = dict(MessageToDict(protobuf, including_default_value_fields=True))

    msg_type_as_list = protobuf_as_dict["@type"].split(".")

    # Remove leading slash
    msg_type_as_list = msg_type_as_list[0][1:]
    protobuf_as_dict.pop("@type")

    value = {re.sub(r"(?<!^)(?=[A-Z])", "_", field).lower(): value for field, value in protobuf_as_dict.items()}
    msg_type = "{root}/{command}".format(
        root=msg_type_as_list[0],
        command=msg_type_as_list[-1].replace("Msg", ""),
    ).replace("cosmos", "cosmos-sdk")

    return {"type": msg_type, "value": value}
