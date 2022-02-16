import os

from pyband.client import Client
from pyband.transaction import Transaction
from pyband.wallet import PrivateKey

from pyband.proto.oracle.v1.tx_pb2 import MsgCreateOracleScript
from google.protobuf.json_format import MessageToJson

def main():
    # Step 1
    #Choose GRPC
    #Laozi Mainnet: laozi1.bandchain.org
    #Laozi Testnet: laozi-testnet4.bandchain.org
    grpc_url = "laozi-testnet4.bandchain.org"
    c = Client(grpc_url)

    # Step 2
    #DO NOT SHARE YOUR mnemonic!!!
    private_key = PrivateKey.from_mnemonic("Enter your mnemonic (Seed Phrases)")
    public_key = private_key.to_public_key()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()
    
    # Step 3
    send_msg = MsgCreateOracleScript(
        sender=sender,
        owner = "Band Address of the Owner",
        name = "Name of the Oracle Script",
        description = "Description of the Oracle Script",
        code = b' The Owasm-compiled binary attached to this Oracle Script \n', #the b'\n' converts your code into Byte
        schema= "The schema detailing the inputs and outputs of this Oracle Script, as well as the corresponding types",
        source_code_url="Url of the Source Code",
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
