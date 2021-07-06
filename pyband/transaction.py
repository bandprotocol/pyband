from typing import List

from google.protobuf import any_pb2
from pyband.proto.cosmos.tx.v1beta1 import tx_pb2 as cosmos_tx_type
from pyband.proto.cosmos.tx.signing.v1beta1 import signing_pb2 as tx_sign

from pyband.client import Client
from pyband.constant import MAX_MEMO_CHARACTERS
from pyband.exceptions import EmptyMsgError, NotFoundError, UndefinedError, ValueTooLargeError


class Transaction:
    def __init__(
        self,
        msgs: List[any_pb2.Any] = None,
        account_num: int = None,
        sequence: int = None,
        chain_id: str = None,
        fee: cosmos_tx_type.Fee = None,
        gas: int = 200000,
        memo: str = "",
    ):
        self.msgs = msgs or []
        self.account_num = account_num
        self.sequence = sequence
        self.chain_id = chain_id
        self.fee = fee
        self.gas = gas
        self.memo = memo

    def with_messages(self, *msgs: any_pb2.Any) -> "Transaction":
        self.msgs.extend(msgs)
        return self

    def with_sender(self, client: Client, sender: str) -> "Transaction":
        if len(self.msgs) == 0:
            raise EmptyMsgError("messsage is empty, please use with_messages at least 1 message")
        account = client.get_account(sender)
        if account:
            self.account_num = account.account_number
            self.sequence = account.sequence
            return self
        raise NotFoundError("Account doesn't exist")

    def with_account_num(self, account_num: int) -> "Transaction":
        self.account_num = account_num
        return self

    def with_sequence(self, sequence: int) -> "Transaction":
        self.sequence = sequence
        return self

    def with_chain_id(self, chain_id: str) -> "Transaction":
        self.chain_id = chain_id
        return self

    def with_fee(self, fee: cosmos_tx_type.Fee) -> "Transaction":
        self.fee = fee
        return self

    def with_gas(self, gas: int) -> "Transaction":
        self.gas = gas
        return self

    def with_memo(self, memo: str) -> "Transaction":
        if len(memo) > MAX_MEMO_CHARACTERS:
            raise ValueTooLargeError("memo is too large")
        self.memo = memo
        return self

    def __generate_info__(self):
        body = cosmos_tx_type.TxBody(
            messages=self.msgs,
            memo=self.memo,
        )

        body_bytes = body.SerializeToString()
        mode_info = cosmos_tx_type.ModeInfo(single=cosmos_tx_type.ModeInfo.Single(mode=tx_sign.SIGN_MODE_DIRECT))
        signer_info = cosmos_tx_type.SignerInfo(mode_info=mode_info, sequence=self.sequence)
        auth_info = cosmos_tx_type.AuthInfo(signer_infos=[signer_info], fee=self.fee)
        auth_info_bytes = auth_info.SerializeToString()

        return body_bytes, auth_info_bytes

    def get_sign_doc(self) -> cosmos_tx_type.SignDoc:
        if len(self.msgs) == 0:
            raise EmptyMsgError("message is empty")

        if self.account_num is None:
            raise UndefinedError("account_num should be defined")

        if self.sequence is None:
            raise UndefinedError("sequence should be defined")

        if self.chain_id is None:
            raise UndefinedError("chain_id should be defined")

        infos = self.__generate_info__()

        sign_doc = cosmos_tx_type.SignDoc(
            body_bytes=infos[0],
            auth_info_bytes=infos[1],
            chain_id=self.chain_id,
            account_number=self.account_num,
        )
        return sign_doc

    def get_tx_data(self, signature: bytes) -> bytes:

        infos = self.__generate_info__()

        tx_raw = cosmos_tx_type.TxRaw(body_bytes=infos[0], auth_info_bytes=infos[1], signatures=[signature])
        tx_raw_bytes = tx_raw.SerializeToString()
        return tx_raw_bytes
