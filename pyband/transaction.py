import json
from typing import List, Tuple, Iterable

from betterproto.lib.google.protobuf import Any as AnyProto

from .client import Client
from .constants import MAX_MEMO_CHARACTERS
from .exceptions import EmptyMsgError, UndefinedError, ValueTooLargeError
from .messages.base import BaseMessageWrapper
from .proto.cosmos.base.v1beta1 import Coin
from .proto.cosmos.tx.signing.v1beta1 import SignMode
from .proto.cosmos.tx.v1beta1 import Fee, TxBody, ModeInfo, SignerInfo, AuthInfo, SignDoc, TxRaw, ModeInfoSingle
from .wallet.public_key import PublicKey


class Transaction:
    def __init__(
        self,
        msgs: List[BaseMessageWrapper] = None,
        account_num: int = None,
        sequence: int = None,
        chain_id: str = None,
        fee: List[Coin] = None,
        gas: int = 200000,
        memo: str = "",
    ):
        self.msgs = msgs if msgs is not None else []
        self.account_num = account_num
        self.sequence = sequence
        self.chain_id = chain_id
        self.fee = Fee(amount=fee, gas_limit=gas)
        self.gas = gas
        self.memo = memo

    @staticmethod
    def __convert_msgs(msgs: Iterable[BaseMessageWrapper]) -> List[AnyProto]:
        return [AnyProto(type_url=msg.type_url, value=bytes(msg)) for msg in msgs]

    def with_messages(self, *msgs: BaseMessageWrapper) -> "Transaction":
        self.msgs.extend(msgs)
        return self

    async def with_sender(self, client: Client, sender: str) -> "Transaction":
        if len(self.msgs) == 0:
            raise EmptyMsgError("message is empty, please use with_messages at least 1 message")

        account = await client.get_account(sender)
        self.account_num = account.account_number
        self.sequence = account.sequence
        return self

    def with_account_num(self, account_num: int) -> "Transaction":
        self.account_num = account_num
        return self

    def with_sequence(self, sequence: int) -> "Transaction":
        self.sequence = sequence
        return self

    def with_chain_id(self, chain_id: str) -> "Transaction":
        self.chain_id = chain_id
        return self

    def with_fee(self, fee: List[Coin]) -> "Transaction":
        self.fee = Fee(amount=fee, gas_limit=self.fee.gas_limit)
        return self

    def with_gas(self, gas: int) -> "Transaction":
        """Sets Transaction's gas.

        Args:
            gas: Gas

        Returns:
            A Transaction instance.
        """

        self.fee.gas_limit = gas
        return self

    def with_memo(self, memo: str) -> "Transaction":
        """Sets Transaction's memo.

        Args:
            memo: Memo with a maximum length of 256.

        Returns:
            A Transaction instance.
        """

        if len(memo) > MAX_MEMO_CHARACTERS:
            raise ValueTooLargeError("memo is too large")
        self.memo = memo
        return self

    def __generate_info(self, public_key: PublicKey, sign_mode: SignMode) -> Tuple[bytes, bytes]:
        body = TxBody(
            messages=self.__convert_msgs(self.msgs),
            memo=self.memo,
        )

        mode_info = ModeInfo(ModeInfoSingle(mode=sign_mode))
        if public_key is not None:
            pub_key_proto = public_key.to_public_key_proto()
            any_public_key = AnyProto(type_url="/cosmos.crypto.secp256k1.PubKey", value=bytes(pub_key_proto))
            signer_info = SignerInfo(mode_info=mode_info, sequence=self.sequence, public_key=any_public_key)
        else:
            signer_info = SignerInfo(mode_info=mode_info, sequence=self.sequence)

        auth_info = AuthInfo(signer_infos=[signer_info], fee=self.fee)

        return bytes(body), bytes(auth_info)

    def get_sign_doc(self, public_key: PublicKey = None) -> SignDoc:
        """Returns the sign data from Transaction.

        Args:
            public_key: A PublicKey instance.

        Returns:
            A SignDoc instance containing the transaction detail.
        """

        if len(self.msgs) == 0:
            raise EmptyMsgError("message is empty")

        if self.account_num is None:
            raise UndefinedError("account_num should be defined")

        if self.sequence is None:
            raise UndefinedError("sequence should be defined")

        if self.chain_id is None:
            raise UndefinedError("chain_id should be defined")

        body_bytes, auth_info_bytes = self.__generate_info(public_key, SignMode.SIGN_MODE_DIRECT)

        return SignDoc(
            body_bytes=body_bytes,
            auth_info_bytes=auth_info_bytes,
            chain_id=self.chain_id,
            account_number=self.account_num,
        )

    def get_sign_message_for_legacy_codec(self) -> bytes:
        """Returns the transaction encoded in Cosmos's legacy format.

        Returns:
            Legacy transaction as byte.
        """

        msg = {
            "account_number": str(self.account_num),
            "chain_id": self.chain_id,
            "fee": {
                "amount": [fee_amount.to_dict() for fee_amount in self.fee.amount],
                "gas": str(self.fee.gas_limit),
            },
            "memo": self.memo,
            "msgs": [msg.to_legacy_codec() for msg in self.msgs],
            "sequence": str(self.sequence),
        }
        return json.dumps(msg, separators=(",", ":"), sort_keys=True).encode("utf-8")

    def get_tx_data(
        self, signature: bytes, public_key: PublicKey = None, sign_mode: SignMode = SignMode.SIGN_MODE_DIRECT
    ) -> bytes:
        """Returns the transaction as a byte.

        Args:
            signature: Signature from get_sign_doc().
            public_key: A public key instance.
            sign_mode: SignMode.

        Returns:
            Transaction as byte.
        """

        body_bytes, auth_info_bytes = self.__generate_info(public_key, sign_mode)
        tx_raw = TxRaw(body_bytes=body_bytes, auth_info_bytes=auth_info_bytes, signatures=[signature])
        return bytes(tx_raw)
