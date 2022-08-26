from pyband.wallet import Ledger
import os

from pyband import Client, Transaction
from pyband.wallet import PrivateKey
from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from google.protobuf.json_format import MessageToJson
from pyband.proto.cosmos.tx.signing.v1beta1 import signing_pb2 as tx_sign


def main():
    # Setup the client
    grpc_url = "laozi-testnet5.bandchain.org"
    # grpc_url = "laozi1.bandchain.org"
    c = Client(grpc_url)

    # Setup the wallet
    ledger = Ledger()
    public_key = ledger.get_public_key()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()
    print(sender)

    # Prepare the transaction's properties
    send_amount = [Coin(amount="1", denom="uband")]
    transfer_msg = MsgSend(
        from_address=sender,
        to_address="band19zpx49n8gyaqrscaklrzynm8sgavfkcmjlap9r",
        amount=send_amount,
    )

    account = c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    fee = [Coin(amount="0", denom="uband")]
    chain_id = c.get_chain_id()

    # Construct the transaction
    txn = (
        Transaction()
        .with_messages(transfer_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas(1000000)
        .with_fee(fee)
    )

    # Sign the Transaction
    sign_msg = txn.get_sign_message()

    test = '{"account_number":"437","chain_id":"band-laozi-testnet5","fee":{"amount":[{"amount":"1000","denom":"uband"}],"gas":"1000000"},"memo":"","msgs":[{"type":"cosmos-sdk/MsgSend","value":{"amount":[{"amount":"1","denom":"uband"}],"from_address":"band1lhw5l38wmk2wqtuh3d7wa7pa6qajstmrdwzj4m","to_address":"band19zpx49n8gyaqrscaklrzynm8sgavfkcmjlap9r"}}],"sequence":"1"}'

    signature = ledger.sign(sign_msg)
    print(f"current_sig: {signature.hex()}")
    print(
        "expected_sig: a989e7cce1f8acc302bdac282756cd05017f641c125d8e262a618808e9197a5507bc7e9f614887ed33b316496f76731e14de4eec5919fbd5185cdfeec9fced24"
    )

    tx_raw_bytes = txn.get_tx_data(signature, public_key, tx_sign.SIGN_MODE_LEGACY_AMINO_JSON)

    tx_block = c.send_tx_block_mode(tx_raw_bytes)

    print(MessageToJson(tx_block))


def main_2():
    from pyband.proto.oracle.v1.tx_pb2 import (
        MsgCreateDataSource,
        MsgCreateOracleScript,
        MsgEditDataSource,
        MsgEditOracleScript,
    )
    from pyband.proto.cosmos.staking.v1beta1.tx_pb2 import MsgDelegate, MsgUndelegate
    from pyband.utils import protobuf_to_json

    grpc_url = "laozi-testnet5.bandchain.org"
    c = Client(grpc_url)

    # ledger = Ledger()
    # public_key = ledger.get_public_key()
    # sender_addr = public_key.to_address()
    # sender = sender_addr.to_acc_bech32()
    sender = "band1lhw5l38wmk2wqtuh3d7wa7pa6qajstmrdwzj4m"

    deploy_ds_msg = MsgCreateDataSource(
        name="abc",
        description="abc",
        executable=b'#!/usr/bin/env python3\nprint("Hello World!")\n',
        fee=[Coin(amount="1", denom="uband")],
        treasury=sender,
        owner=sender,
        sender=sender,
    )

    import base64

    edit_ds_msg = MsgEditDataSource(
        data_source_id=426,
        name="[do-not-modify]",
        description="edited v2",
        executable="[do-not-modify]".encode(),
        fee=[],
        treasury=sender,
        owner=sender,
        sender=sender,
    )

    deploy_os_msg = MsgCreateOracleScript(
        name="Hello World!",
        schema="{repeat:u64}/{response:string}",
        code=open("hello_world.wasm", "rb").read(),
        owner=sender,
        sender=sender,
    )

    edit_os_msg = MsgEditOracleScript(oracle_script_id=304, owner=sender, sender=sender, description="edited")

    transfer_msg = MsgSend(
        from_address=sender,
        to_address="band19zpx49n8gyaqrscaklrzynm8sgavfkcmjlap9r",
        amount=[Coin(amount="1", denom="uband")],
    )

    # account = c.get_account(sender)
    # account_num = account.account_number
    account_num = 437

    # sequence = account.sequence
    sequence = 2

    fee = [Coin(amount="0", denom="uband")]
    chain_id = c.get_chain_id()
    # chain_id = "band-laozi-testnet5"

    # Construct the transaction
    txn = (
        Transaction()
        .with_messages(edit_ds_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas(1000000)
        .with_fee(fee)
    )
    sign_msg = txn.get_sign_message()
    print(sign_msg)

    # signature = ledger.sign(sign_msg)

    tx_raw_bytes = txn.get_tx_data(signature, public_key, tx_sign.SIGN_MODE_LEGACY_AMINO_JSON)
    tx_block = c.send_tx_block_mode(tx_raw_bytes)
    print(MessageToJson(tx_block))
    # {"account_number":"437","chain_id":"band-laozi-testnet5","fee":{"amount":[{"amount":"1000","denom":"uband"}],"gas":"1000000"},"memo":"","msgs":[{"type":"cosmos-sdk/MsgSend","value":{"amount":[{"amount":"1","denom":"uband"}],"from_address":"band1lhw5l38wmk2wqtuh3d7wa7pa6qajstmrdwzj4m","to_address":"band19zpx49n8gyaqrscaklrzynm8sgavfkcmjlap9r"}}],"sequence":"1"}
    # type oracle/EditDataSource
    # msgs/value/data_source 32
    # Description [do-not-modify]
    # msg/value/execute
    # msg/value/fee
    # msgs/value/name [do-not-modify]


if __name__ == "__main__":
    main_2()
    # print(open("python.py").read().encode())

# 7B2872FB929F45CBCB52A6B117CCFE66D0FCE23C7799250A8C1F632E61B23D1C
