from .address import Address
from .constants import DEFAULT_DERIVATION_PATH, DEFAULT_LEDGER_DERIVATION_PATH
from .private_key import PrivateKey
from .public_key import PublicKey
from .signer import Signer, PrivateKeySigner, LedgerSigner
from ..cosmos_app import CosmosApp
from ..proto.cosmos.tx.signing.v1beta1 import SignMode
from ..transaction import Transaction
from ..utils import bip44_to_list


class Wallet:
    def __init__(self, signer: Signer, sign_mode: SignMode):
        self._signer = signer
        self._sign_mode = sign_mode

    @classmethod
    def from_mnemonic(cls, mnemonic: str, path: str = DEFAULT_DERIVATION_PATH):
        """Creates a Wallet instance from a mnemonic phrase and derivation path.

        Args:
            mnemonic: The mnemonic phrase.
            path: The derivation path. If omitted, defaults to Band's default HD prefix.

        Returns:
            A Wallet instance.
        """

        return cls(PrivateKeySigner(PrivateKey.from_mnemonic(mnemonic, path)), SignMode.SIGN_MODE_DIRECT)

    @classmethod
    def from_private_key(cls, private_key: str):
        """Creates a Wallet instance from a hexadecimal private key.

        Args:
            private_key: A private key represented as a hexadecimal.

        Returns:
            A Wallet instance.
        """

        return cls(PrivateKeySigner(PrivateKey.from_hex(private_key)), SignMode.SIGN_MODE_DIRECT)

    @classmethod
    def from_ledger(cls, path: str = DEFAULT_LEDGER_DERIVATION_PATH, *, app: CosmosApp = None):
        """Creates a Wallet instance from a connected Ledger.

        Args:
            path: The derivation path. If omitted, defaults to Cosmos's default HD prefix.
            app: A CosmosApp instance.

        Returns:
            A Wallet instance.
        """

        return cls(
            LedgerSigner(path=path, app=app if app is not None else CosmosApp(bip44_to_list(path))),
            SignMode.SIGN_MODE_LEGACY_AMINO_JSON,
        )

    def get_public_key(self) -> PublicKey:
        """Gets the public key associated with this wallet

        Returns:
            A PublicKey instance
        """

        return self._signer.get_public_key()

    def get_address(self) -> Address:
        """Gets the address associated with this wallet

        Returns:
            An Address instance
        """

        return self._signer.get_address()

    def sign_and_build(self, tx: Transaction) -> bytes:
        """Signs and builds a broadcastable transaction.

        Args:
            tx: A transaction instance to create a broadcastable transaction from.

        Returns:
            A transaction as bytes.
        """
        public_key = self.get_public_key()

        if self._sign_mode == SignMode.SIGN_MODE_LEGACY_AMINO_JSON:
            sign_msg = tx.get_sign_message_for_legacy_codec()
        else:
            sign_msg = tx.get_sign_doc(public_key)

        signature = self._signer.sign(bytes(sign_msg))
        return tx.get_tx_data(signature, public_key, sign_mode=self._sign_mode)
