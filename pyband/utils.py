import re
import math

from typing import List
from .exceptions import NotBip44Error, IncorrectLengthError


def is_bip44(derivation_path: str) -> bool:
    if re.search("m/\d+'/\d+'+/\d+'/\d+/\d+$", derivation_path) is not None:
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
    chunk_size = 250
    packet_count = math.ceil(len(byte_message) / chunk_size)

    output = []
    for i in range(0, packet_count * chunk_size, chunk_size):
        output.append(byte_message[i : i + chunk_size])
    return output
