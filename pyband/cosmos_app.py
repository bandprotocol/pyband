from dataclasses import dataclass, fields
from typing import Optional, NoReturn
from ledgerblue.comm import getDongle
from ledgerblue.commException import CommException
from pyband.exceptions import CosmosAppError
from pyband.utils import get_bip32_byte, split_packet


@dataclass
class CosmosAppCommand:
    CLA: bytes
    INS: bytes
    P1: bytes
    P2: bytes
    L: Optional[bytes] = None
    data: Optional[bytes] = None

    def __post_init__(self):
        self.set_l()

    def set_l(self):
        if self.data is None:
            self.L = b"\x00"
        else:
            self.L = len(self.data).to_bytes(1, "little")

    def get_message(self):
        message = b""
        for field in fields(self.__class__):
            field_value = getattr(self, field.name)
            if field_value is not None:
                message += field_value
        return message


class CosmosAppResults:
    def __iter__(self):
        for var in self.__slots__:
            yield getattr(self, var)


class AppVersion(CosmosAppResults):
    __slots__ = ("cla", "major", "minor", "patch")

    def __init__(self, cla: int, major: int, minor: int, patch: int):
        self.cla = cla
        self.major = major
        self.minor = minor
        self.patch = patch

    def __repr__(self):
        return "AppVersion(cla={}, major={}, minor={}, patch={})".format(*self.__iter__())


class SepcAddr(CosmosAppResults):
    __slots__ = ("public_key", "address")

    def __init__(self, public_key: bytes, address: bytes):
        self.public_key = public_key
        self.address = address

    def __repr__(self):
        return "SepcAddr(public_key={}, address={})".format(*self.__iter__())


class CosmosApp:
    def __init__(self, derivation_path):
        self._dongle = getDongle()
        self._derivation_path = derivation_path

    def disconnect(self) -> NoReturn:
        self._dongle.close()

    def get_version(self) -> AppVersion:
        command = CosmosAppCommand(
            CLA=b"\x55",
            INS=b"\x00",
            P1=b"\x00",
            P2=b"\x00",
        )

        try:
            resp = self._dongle.exchange(command.get_message())
        except CommException as e:
            raise CosmosAppError(hex(e.sw))
        return AppVersion(*(resp[i] for i in range(4)))

    def ins_get_addr_secp256k1(self, hrp: str, req_confirm: bool = True) -> SepcAddr:
        try:
            bip32_byte = get_bip32_byte(self._derivation_path, 3)
        except Exception as e:
            raise e

        command = CosmosAppCommand(
            CLA=b"\x55",
            INS=b"\x04",
            P1=req_confirm.to_bytes(1, "little"),
            P2=b"\x00",
            data=len(hrp).to_bytes(1, "little") + hrp.encode() + bip32_byte,
        )

        try:
            resp = self._dongle.exchange(command.get_message())
            print(resp)
        except CommException as e:
            raise CosmosAppError(hex(e.sw))
        return SepcAddr(resp[:33], resp[33:])

    def sign_secp256k1(self, msg: bytes) -> bytes:
        command = CosmosAppCommand(
            CLA=b"\x55",
            INS=b"\x02",
            P1=b"\x00",
            P2=b"\x00",
            data=get_bip32_byte(self._derivation_path, 3),
        )
        try:
            resp = self._dongle.exchange(command.get_message())
        except CommException as e:
            raise CosmosAppError(hex(e.sw))

        packets = split_packet(msg)
        for i, packet in enumerate(packets):
            if i == len(packets) - 1:
                payload_desc = b"\x02"
            else:
                payload_desc = b"\x01"
            command = CosmosAppCommand(
                CLA=b"\x55",
                INS=b"\x02",
                P1=payload_desc,
                P2=b"\x00",
                data=packet,
            )
            try:
                resp = self._dongle.exchange(command.get_message())
            except CommException as e:
                raise CosmosAppError(hex(e.sw))
        return resp
