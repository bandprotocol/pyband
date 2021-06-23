from .wallet import PrivateKey
from .constant import MAX_MEMO_CHARACTERS
from .exceptions import EmptyMsgError, NotFoundError, UndefinedError, ValueTooLargeError
from google.protobuf import any_pb2
from pyband.proto.oracle.v1 import tx_pb2 as tx_oracle_type
from pyband.proto.cosmos.tx.v1beta1 import tx_pb2 as cosmos_tx_type
from pyband.proto.cosmos.tx.signing.v1beta1 import signing_pb2 as tx_sign


class Transaction:
    def __init__(self):
        self.msgs: List[any_pb2.Any] = []
        self.account_num: Optional[int] = None
        self.sequence: Optional[int] = None
        self.chain_id: Optional[str] = None
        self.fee: cosmos_tx_type.Fee = None
        self.gas: int = 200000
        self.memo: str = ""

    def with_messages(self, *msgs: [tx_oracle_type.MsgRequestData]) -> "Transaction":
        msg_any = any_pb2.Any()
        for msg in msgs:
            msg_any.Pack(msg, type_url_prefix="")
            self.msgs.append(msg_any)
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

    def get_tx_data(self, privateKey: PrivateKey) -> bytes:
        if len(self.msgs) == 0:
            raise EmptyMsgError("message is empty")

        if self.account_num is None:
            raise UndefinedError("account_num should be defined")

        if self.sequence is None:
            raise UndefinedError("sequence should be defined")

        if self.chain_id is None:
            raise UndefinedError("chain_id should be defined")

        body = cosmos_tx_type.TxBody(
            messages=self.msgs,
            memo=self.memo,
        )

        body_bytes = body.SerializeToString()

        mode_info = cosmos_tx_type.ModeInfo(single=cosmos_tx_type.ModeInfo.Single(mode=tx_sign.SIGN_MODE_DIRECT))

        signer_info = cosmos_tx_type.SignerInfo(mode_info=mode_info, sequence=self.sequence)

        auth_info = cosmos_tx_type.AuthInfo(signer_infos=[signer_info], fee=self.fee)
        auth_info_bytes = auth_info.SerializeToString()

        # Sign data
        sign_doc = cosmos_tx_type.SignDoc(
            body_bytes=body_bytes,
            auth_info_bytes=auth_info_bytes,
            chain_id=self.chain_id,
            account_number=self.account_num,
        )

        signature = privateKey.sign(sign_doc.SerializeToString())
        tx_raw = cosmos_tx_type.TxRaw(body_bytes=body_bytes, auth_info_bytes=auth_info_bytes, signatures=[signature])
        tx_raw_bytes = tx_raw.SerializeToString()
        return tx_raw_bytes
