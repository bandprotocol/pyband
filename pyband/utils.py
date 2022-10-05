import re
from typing import List

from .exceptions import NotBip44Error, IncorrectLengthError


def is_bip44(derivation_path: str) -> bool:
    """Checks if the given derivation path is a valid bip44 path.

    Args:
        derivation_path: Derivation path as a string

    Returns:
        Whether the path is valid or not
    """
    if re.search("^m(/[0-9]+['hH]?)*$", derivation_path) is not None:
        return True
    else:
        return False


def bip44_to_list(derivation_path: str) -> List[int]:
    """Converts the given string formatted derivation path into a list
    Args:
        derivation_path: Derivation path as a string

    Returns:
        Derivation path as a list

    Raises:
        NotBip44Error: If derivation path is not valid
    """
    try:
        return [int(x) for x in derivation_path.replace("'", "").split("/")[1:]]
    except ValueError:
        raise NotBip44Error()
    except Exception as e:
        raise e


def get_bip32_byte(derivation_path: List[int], harden_count: int) -> bytes:
    """Encodes BIP32 as a byte

    Args:
        derivation_path: The derivation path as a list
        harden_count: The depth level of keys to harden

    Returns:
        BIP32 as a byte
    """
    if len(derivation_path) != 5:
        raise IncorrectLengthError("Incorrect path length")

    path_bytes = b""
    for i, idx in enumerate(derivation_path):
        if i < harden_count:
            idx = 0x80000000 | idx
        path_bytes += idx.to_bytes(4, "little")
    return path_bytes


def split_packet(byte_message: bytes) -> List[bytes]:
    """
    Splits a message into packets of size 250 bytes each

    Args:
        byte_message: Message as in bytes

    Returns:
        Message split into packets
    """
    return [bytes(byte_message[i : i + 250]) for i in range(0, len(byte_message), 250)]
