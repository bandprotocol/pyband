import hashlib
from typing import Tuple, Optional

from bip32 import BIP32
from ecdsa.curves import SECP256k1
from ecdsa.keys import SigningKey
from ecdsa.util import sigencode_string_canonize
from mnemonic import Mnemonic

from .constants import DEFAULT_DERIVATION_PATH
from .public_key import PublicKey


class PrivateKey:
    """Class for wrapping SigningKey, used to sign messages and derive the associated public key.

    Attributes:
        signing_key: The ecdsa SigningKey instance.
    """

    def __init__(self, _error_do_not_use_init_directly=None) -> None:
        """Unsupported, please use from_mnemonic to initialize."""

        if not _error_do_not_use_init_directly:
            raise TypeError("Please use PrivateKey.from_mnemonic() to construct me")
        self.signing_key: Optional[SigningKey] = None

    @classmethod
    def generate(cls, path=DEFAULT_DERIVATION_PATH) -> Tuple[str, "PrivateKey"]:
        """Generates a new private key with a derivation path and random mnemonic phrase.

        Args:
            path: The derivation path, if omitted, defaults to Band's default HD prefix 494 with all other indexes being zeroes.

        Returns:
            A tuple containing the mnemonic phrase and the PrivateKey instance.
        """

        phrase = Mnemonic(language="english").generate(strength=256)
        return phrase, cls.from_mnemonic(phrase, path)

    @classmethod
    def from_mnemonic(cls, words: str, path=DEFAULT_DERIVATION_PATH) -> "PrivateKey":
        """Create a PrivateKey instance from a given mnemonic phrase and derivation path.

        Args:
            words: The mnemonic phrase.
            path: The derivation path, if omitted, defaults to Band's default HD prefix 494 with all other indexes being zeroes.

        Returns:
            A PrivateKey instance.
        """

        seed = Mnemonic("english").to_seed(words)
        self = cls(_error_do_not_use_init_directly=True)
        self.signing_key = SigningKey.from_string(
            BIP32.from_seed(seed).get_privkey_from_path(path), curve=SECP256k1, hashfunc=hashlib.sha256
        )
        return self

    @classmethod
    def from_hex(cls, priv: str) -> "PrivateKey":
        """Create a PrivateKey instance from a hex representation of the signing key.

        Args:
            priv: A hex representation of the signing key.

        Returns:
            A PrivateKey instance.
        """

        self = cls(_error_do_not_use_init_directly=True)
        self.signing_key = SigningKey.from_string(bytes.fromhex(priv), curve=SECP256k1, hashfunc=hashlib.sha256)
        return self

    def to_hex(self) -> str:
        """Returns a hex representation of the signing key.

        Returns:
            A hex representation of signing key.
        """

        return self.signing_key.to_string().hex()

    def to_public_key(self) -> PublicKey:
        """Gets the associated PublicKey.

        Returns:
            A PublicKey instance associated with the object's PrivateKey.
        """

        public_key = PublicKey(_error_do_not_use_init_directly=True)
        public_key.verify_key = self.signing_key.get_verifying_key()
        return public_key

    def sign(self, msg: bytes) -> bytes:
        """Sign the given message using the edcsa sign_deterministic function.

        Args:
            msg: Message to be signed and hashed.

        Returns:
            A signature of this private key over the given message.
        """

        return self.signing_key.sign_deterministic(msg, hashfunc=hashlib.sha256, sigencode=sigencode_string_canonize)
