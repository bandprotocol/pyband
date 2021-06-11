from .wallet import PublicKey
from google.protobuf import any_pb2
from .constant import MAX_MEMO_CHARACTERS
from .exceptions import EmptyMsgError, NotFoundError, UndefinedError, ValueTooLargeError
from pyband.cosmos.tx.v1beta1 import tx_pb2 as tx_type
from pyband.cosmos.tx.signing.v1beta1 import signing_pb2 as tx_sign
from google.protobuf import any_pb2


class Trans:
    def __init__(self):
        self.msgs: List[google.protobuf.any_pb2] = []       # protobuf.any
        self.account_num: Optional[int] = None  # int
        self.sequence: Optional[int] = None     # int
        self.chain_id: Optional[str] = None     # str
        self.fee: int = 0                       # int
        self.gas: int = 200000                  # int
        self.memo: str = ""                     # str

    def with_messages(self, *msgs) -> "Transaction":
        msg_any = any_pb2.Any()
        for msg in msgs:
            print(msg)
        
            msg_any.Pack(msg, type_url_prefix="")
            self.msgs.append(msg_any)
        # msg_any.Pack(msgs, type_url_prefix="")
        # self.msgs = msg_any
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

    def with_fee(self, fee: int) -> "Transaction":
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

    def get_tx_data(self, privateKey, gas_limit) -> bytes:
        body = tx_type.TxBody(
            messages=self.msgs,
            memo=self.memo,
        )
        body_bytes = body.SerializeToString()

        mode_info = tx_type.ModeInfo(
            single=tx_type.ModeInfo.Single(mode=tx_sign.SIGN_MODE_DIRECT))

        signer_info = tx_type.SignerInfo(mode_info=mode_info, sequence=self.sequence)
        fee = tx_type.Fee(amount=[], gas_limit=gas_limit) 
        
        auth_info = tx_type.AuthInfo(signer_infos=[signer_info], fee=fee)
        auth_info_bytes = auth_info.SerializeToString()

        # Sign data
        sign_doc = tx_type.SignDoc(
            body_bytes=body_bytes, auth_info_bytes=auth_info_bytes, chain_id=self.chain_id, account_number=self.account_num)

        signature = privateKey.sign(sign_doc.SerializeToString())
        tx_raw = tx_type.TxRaw(
            body_bytes=body_bytes, auth_info_bytes=auth_info_bytes, signatures=[signature])
        tx_raw_bytes = tx_raw.SerializeToString()
        return tx_raw_bytes

