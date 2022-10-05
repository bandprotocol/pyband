import math
import pytest

from pyband.utils import is_bip44, bip44_to_list, get_bip32_byte, split_packet, NotBip44Error


@pytest.fixture
def valid_path():
    return "m/44'/118'/0'/0/0"


@pytest.fixture
def invalid_paths():
    return ["m/a'/b'/c'/d/e", "/44'/118'/0'/0/0"]


def test_is_bip44_success(valid_path):
    assert is_bip44(valid_path) is True


def test_is_bip44_failure(invalid_paths):
    assert [is_bip44(x) for x in invalid_paths] == [False] * len(invalid_paths)


def test_bip44_to_list_success(valid_path):
    assert bip44_to_list(valid_path) == [44, 118, 0, 0, 0]


def test_bip44_to_list_failure(invalid_paths):
    with pytest.raises(NotBip44Error):
        bip44_to_list(invalid_paths[0])


def test_get_bip32_byte(valid_path):
    path_list = bip44_to_list(valid_path)
    expected_val = b"\x2c\x00\x00\x80\x76\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x80"
    assert get_bip32_byte(path_list, 5) == expected_val


def test_split_packet():
    test_msg_size = 1111
    expected_packet_size = 250
    test_msg = b"0" * test_msg_size

    expected_packets_count = math.ceil(test_msg_size / expected_packet_size)
    packets = split_packet(test_msg)

    assert len(packets) == expected_packets_count
    assert packets[0] == b"0" * expected_packet_size
    assert packets[-1] == b"0" * (test_msg_size % expected_packet_size)
