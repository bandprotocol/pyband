from abc import abstractmethod

from ecdsa.der import remove_sequence, UnexpectedDER, remove_integer

from .address import Address
from .constants import BECH32_ADDR_ACC_PREFIX
from .private_key import PrivateKey
from .public_key import PublicKey
from ..cosmos_app import CosmosApp
from ..utils import bip44_to_list


class Signer:
    @abstractmethod
    def get_public_key(self) -> PublicKey:
        """Gets public key associated with the signer.

        Returns:
            A PublicKey instance.
        """

        pass

    @abstractmethod
    def get_address(self) -> Address:
        """Gets address associated with the signer.

        Returns:
            An Address instance.
        """

        pass

    @abstractmethod
    def sign(self, msg: bytes) -> bytes:
        """Signs a message with the signer.

        Args:
            msg: The message to sign in bytes.

        Returns:
            Signature in bytes.
        """

        pass


class PrivateKeySigner(Signer):
    def __init__(self, private_key: PrivateKey):
        self.private_key = private_key

    def get_public_key(self) -> PublicKey:
        return self.private_key.to_public_key()

    def get_address(self) -> Address:
        return self.private_key.to_public_key().to_address()

    def sign(self, msg: bytes) -> bytes:
        return self.private_key.sign(bytes(msg))


class LedgerSigner(Signer):
    def __init__(self, path: str, app: CosmosApp):
        self.cosmos_app = app if app is not None else CosmosApp(bip44_to_list(path))

    def get_public_key(self) -> PublicKey:
        return PublicKey.from_hex(self.cosmos_app.ins_get_addr_secp256k1(BECH32_ADDR_ACC_PREFIX, False).public_key)

    def get_address(self) -> Address:
        return Address.from_acc_bech32(
            self.cosmos_app.ins_get_addr_secp256k1(BECH32_ADDR_ACC_PREFIX, False).address.decode()
        )

    def sign(self, msg: bytes) -> bytes:
        data, remaining_data = remove_sequence(self.cosmos_app.sign_secp256k1(msg))
        if remaining_data:
            raise UnexpectedDER("Unexpected remainder")

        r, remaining_content = remove_integer(data)
        s, remaining_content = remove_integer(remaining_content)
        if remaining_content:
            raise UnexpectedDER("Unexpected remainder")

        return r.to_bytes(32, "big") + s.to_bytes(32, "big")
