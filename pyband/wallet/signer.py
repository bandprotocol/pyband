from abc import abstractmethod

from ecdsa.der import remove_sequence, UnexpectedDER, remove_integer

from .address import Address
from .private_key import PrivateKey
from .public_key import PublicKey
from ..cosmos_app import CosmosApp
from ..utils import bip44_to_list


class Signer:
    def __init__(self):
        self.public_key = self.get_public_key()
        self.address = self.get_address()

    @abstractmethod
    def get_public_key(self) -> PublicKey:
        """

        Returns:

        """
        pass

    @abstractmethod
    def get_address(self) -> Address:
        """

        Returns:

        """
        pass

    @abstractmethod
    def sign(self, msg: bytes) -> bytes:
        """

        Args:
            msg:

        Returns:

        """
        pass


class PrivateKeySigner(Signer):
    def __init__(self, private_key: PrivateKey):
        self.private_key = private_key
        super().__init__()

    def get_public_key(self) -> PublicKey:
        return self.private_key.to_public_key()

    def get_address(self) -> Address:
        return self.public_key.to_address()

    def sign(self, msg: bytes) -> bytes:
        return self.private_key.sign(bytes(msg))


class LedgerSigner(Signer):
    def __init__(self, path: str, app: CosmosApp):
        self.cosmos_app = app if app is not None else CosmosApp(bip44_to_list(path))
        super().__init__()

    def get_public_key(self) -> PublicKey:
        return PublicKey.from_hex(self.cosmos_app.ins_get_addr_secp256k1("band", False).public_key)

    def get_address(self) -> Address:
        return Address.from_acc_bech32(self.cosmos_app.ins_get_addr_secp256k1("band").address.decode())

    def sign(self, msg: bytes) -> bytes:
        data, remaining_data = remove_sequence(self.cosmos_app.sign_secp256k1(msg))
        if remaining_data:
            raise UnexpectedDER("Unexpected remainder")

        r, remaining_content = remove_integer(data)
        s, remaining_content = remove_integer(remaining_content)
        if remaining_content:
            raise UnexpectedDER("Unexpected remainder")

        return r.to_bytes(32, "big") + s.to_bytes(32, "big")
