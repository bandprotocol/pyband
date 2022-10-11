from bech32 import bech32_encode, bech32_decode, convertbits

from .constants import BECH32_ADDR_ACC_PREFIX, BECH32_ADDR_CONS_PREFIX, BECH32_ADDR_VAL_PREFIX
from ..exceptions import ConvertError, DecodeError


class Address:
    """Class for wrapping address. Contains methods to encode or decode Bech32.

    Attributes:
        addr:
    """

    def __init__(self, addr: bytes) -> None:
        self.addr = addr

    def __eq__(self, o: "Address") -> bool:
        return self.addr == o.addr

    @classmethod
    def _from_bech32(cls, bech: str, prefix: str) -> "Address":
        hrp, bz = bech32_decode(bech)
        assert hrp == prefix, "Invalid bech32 prefix"
        if bz is None:
            raise DecodeError("Cannot decode bech32")
        eight_bit_r = convertbits(bz, 5, 8, False)
        if eight_bit_r is None:
            raise ConvertError("Cannot convert to 8 bit")

        return cls(bytes(eight_bit_r))

    @classmethod
    def from_acc_bech32(cls, bech: str) -> "Address":
        """Creates an address instance from a bech32 account address.

        Args:
            bech: Bech32 account address.

        Returns:
            An Address instance.
        """

        return cls._from_bech32(bech, BECH32_ADDR_ACC_PREFIX)

    @classmethod
    def from_val_bech32(cls, bech: str) -> "Address":
        """Creates an address instance from a bech32 validator address.

        Args:
            bech: Bech32 validator address.

        Returns:
            An Address instance.
        """

        return cls._from_bech32(bech, BECH32_ADDR_VAL_PREFIX)

    @classmethod
    def from_cons_bech32(cls, bech: str) -> "Address":
        """Creates an address instance from a bech32 validator consensus address.

        Args:
            bech: Bech32 validator consensus address.

        Returns:
            An Address instance.
        """

        return cls._from_bech32(bech, BECH32_ADDR_CONS_PREFIX)

    def _to_bech32(self, prefix: str) -> str:
        five_bit_r = convertbits(self.addr, 8, 5)
        assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
        return bech32_encode(prefix, five_bit_r)

    def to_acc_bech32(self) -> str:
        """Returns a bech32 account address.

        Returns:
            A bech32 address as a string.
        """

        return self._to_bech32(BECH32_ADDR_ACC_PREFIX)

    def to_val_bech32(self) -> str:
        """Returns a bech32 validator address.

        Returns:
            A bech32 address as a string.
        """

        return self._to_bech32(BECH32_ADDR_VAL_PREFIX)

    def to_cons_bech32(self) -> str:
        """Returns a bech32 validator consensus address.

        Returns:
            A bech32 address as a string.
        """

        return self._to_bech32(BECH32_ADDR_CONS_PREFIX)

    def to_hex(self) -> str:
        """Returns a hex representation of the address.

        Returns:
            A hex representation of address.
        """

        return self.addr.hex()
