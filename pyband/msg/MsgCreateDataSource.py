import os

from pyband.client import Client
from pyband.transaction import Transaction
from pyband.wallet import PrivateKey

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.oracle.v1.tx_pb2 import MsgCreateDataSource
from google.protobuf.json_format import MessageToJson

def main():
    # Step 1
    #Choose GRPC
    #Laozi Mainnet: laozi1.bandchain.org
    #Laozi Testnet: laozi-testnet4.bandchain.org
    grpc_url = "laozi1.bandchain.org"
    c = Client(grpc_url)

    # Step 2
    #DO NOT SHARE YOUR mnemonic!!!
    private_key = PrivateKey.from_mnemonic("Enter your mnemonic (Seed Phrases)")
    public_key = private_key.to_public_key()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()
    
    # Step 3
    send_msg = MsgCreateDataSource(
        sender=sender,
        owner = "Band Address of the Owner",
        treasury = "Band Address of the Treasury",
        name = "Name of the Data Source",
        description = "Description of the Data Source",
        fee = [Coin(amount="Fee per single request", denom="uband")], #1000000 Uband is one Band
        executable = b' Paste your Code (Executable) in here \n', #the b'\n' converts your code into []Byte
    )

    account = c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    chain_id = c.get_chain_id()

    # Step 4
    txn = (
        Transaction()
        .with_messages(send_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas(2000000)
        .with_memo("")
    )

    # Step 5
    sign_doc = txn.get_sign_doc(public_key)
    signature = private_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = txn.get_tx_data(signature, public_key)

    # Step 6
    tx_block = c.send_tx_block_mode(tx_raw_bytes)
    print(MessageToJson(tx_block))

if __name__ == "__main__":
    main()
