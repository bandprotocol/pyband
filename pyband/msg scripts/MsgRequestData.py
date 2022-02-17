import os

from pyband.client import Client
from pyband.transaction import Transaction
from pyband.wallet import PrivateKey

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.oracle.v1.tx_pb2 import MsgRequestData
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
    send_msg = MsgRequestData(
        oracle_script_id = "Oracle Script ID from any existing Oracle you wish to get Data from without Quotation Marks (int)",
        sender = sender,
        calldata = "The data passed over to the oracle script for the script to use during its execution (string)",
        ask_count = "Number of validators requested to answer the request without Quotation Marks (int)",
        min_count = "The minimum number of validators necessary for the request to proceed to the execution phase without Quotation Marks (int)",
        client_id = "The unique identifier of this oracle request, as specified by the client. This same unique ID will be sent back to the requester with the oracle response (string)",
    )

    account = c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    fee = [Coin(amount="10000", denom="uband")]
    chain_id = c.get_chain_id()

    # Step 4
    txn = (
        Transaction()
        .with_messages(send_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas(2000000)
        .with_fee(fee)
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
