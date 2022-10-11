import hashlib
from typing import Optional

from bech32 import bech32_decode, convertbits, bech32_encode
from ecdsa.curves import SECP256k1
from ecdsa.keys import VerifyingKey, BadSignatureError

from .address import Address
from .constants import BECH32_PUBKEY_ACC_PREFIX, BECH32_PUBKEY_VAL_PREFIX, BECH32_PUBKEY_CONS_PREFIX
from ..exceptions import DecodeError
from ..proto.cosmos.crypto.secp256k1 import PubKey as PubKeyProto


class PublicKey:
    """Class for wrapping VerifyKey used for signature verification. Contains methods to encode or decode Bech32.

    Attributes:
        verify_key: the ecdsa VerifyingKey instance
    """

    def __init__(self, _error_do_not_use_init_directly=None) -> None:
        """Unsupported, please do not construct it directly."""

        if not _error_do_not_use_init_directly:
            raise TypeError("Please use PublicKey's factory methods to construct me")
        self.verify_key: Optional[VerifyingKey] = None

    @classmethod
    def _from_bech32(cls, bech: str, prefix: str) -> "PublicKey":
        hrp, bz = bech32_decode(bech)
        assert hrp == prefix, "Invalid bech32 prefix"
        if bz is None:
            raise DecodeError("Cannot decode bech32")
        bz = convertbits(bz, 5, 8, False)
        self = cls(_error_do_not_use_init_directly=True)
        self.verify_key = VerifyingKey.from_string(bytes(bz[5:]), curve=SECP256k1, hashfunc=hashlib.sha256)
        return self

    @classmethod
    def from_acc_bech32(cls, bech: str) -> "PublicKey":
        """Creates a PublicKey from a bech32 string with an account public key prefix.

        Args:
            bech: Bech32 string with an account public key prefix.

        Returns:
            A PublicKey instance.
        """

        return cls._from_bech32(bech, BECH32_PUBKEY_ACC_PREFIX)

    @classmethod
    def from_val_bech32(cls, bech: str) -> "PublicKey":
        """Creates a PublicKey from a bech32 string with a validator public key prefix.

        Args:
            bech: Bech32 string with a validator public key prefix.

        Returns:
            A PublicKey instance.
        """

        return cls._from_bech32(bech, BECH32_PUBKEY_VAL_PREFIX)

    @classmethod
    def from_cons_bech32(cls, bech: str) -> "PublicKey":
        """Creates a PublicKey from a bech32 string with a validator consensus public key prefix.

        Args:
            bech: Bech32 string with a validator consensus public key prefix.

        Returns:
            A PublicKey instance.
        """

        return cls._from_bech32(bech, BECH32_PUBKEY_CONS_PREFIX)

    @classmethod
    def from_hex(cls, pub: bytes) -> "PublicKey":
        """Creates a PublicKey from a hex representation of the verifying key.

        Args:
            pub: A hex representation of the verifying key.

        Returns:
            A PublicKey instance.
        """

        self = cls(_error_do_not_use_init_directly=True)
        self.verify_key = VerifyingKey.from_string(pub, curve=SECP256k1, hashfunc=hashlib.sha256)
        return self

    def to_hex(self) -> str:
        """Returns a hex representation of the verifying key.

        Returns:
            A hex representation of verified key.
        """

        return self.verify_key.to_string("compressed").hex()

    def to_public_key_proto(self) -> PubKeyProto:
        """Returns a public key of type protobuf.

        Returns:
            A PubKeyProto instance.
        """

        return PubKeyProto(key=self.verify_key.to_string("compressed"))

    def _to_bech32(self, prefix: str) -> str:
        five_bit_r = convertbits(
            # Append prefix public key type follow amino spec.
            bytes.fromhex("eb5ae98721") + self.verify_key.to_string("compressed"),
            8,
            5,
        )
        assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
        return bech32_encode(prefix, five_bit_r)

    def to_acc_bech32(self) -> str:
        """Returns a bech32 string with an account public key prefix.

        Returns:
            A bech32 address as a string.
        """

        return self._to_bech32(BECH32_PUBKEY_ACC_PREFIX)

    def to_val_bech32(self) -> str:
        """Returns a bech32 string with a validator public key prefix.

        Returns:
            A bech32 address as a string.
        """

        return self._to_bech32(BECH32_PUBKEY_VAL_PREFIX)

    def to_cons_bech32(self) -> str:
        """Returns a bech32 string with a validator consensus public key prefix.

        Returns:
            A bech32 address as a string.
        """

        return self._to_bech32(BECH32_PUBKEY_CONS_PREFIX)

    def to_address(self) -> Address:
        """Return address instance from this public key.

        Returns:
            An Address instance.
        """

        hash = hashlib.new("sha256", self.verify_key.to_string("compressed")).digest()
        return Address(hashlib.new("ripemd160", hash).digest())

    def verify(self, msg: bytes, sig: bytes) -> bool:
        """Verify a signature made from the given message.

        Args:
            msg: Data signed by the signature.
            sig: The encoded signature.

        Raises:
            BadSignatureError: If the signature is invalid or malformed.

        Returns:
            True if the verification was successful, false otherwise.
        """

        try:
            return self.verify_key.verify(sig, msg, hashfunc=hashlib.sha256)
        except BadSignatureError:
            return False
