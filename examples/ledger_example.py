from pyband.wallet import Ledger

from pyband import Client, Transaction

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.oracle.v1.tx_pb2 import MsgEditDataSource
from pyband.proto.cosmos.tx.signing.v1beta1 import signing_pb2 as tx_sign
from google.protobuf.json_format import MessageToJson


def main():
    # Create the gRPC connectioj
    grpc_url = "laozi-testnet5.bandchain.org"
    c = Client(grpc_url)

    # Get the public key and sender from the ledger
    ledger = Ledger()
    public_key = ledger.get_public_key()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()

    # Prepare the transaction's properties
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

    account = c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    fee = [Coin(amount="0", denom="uband")]
    chain_id = c.get_chain_id()

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

    # Sign the transaction using the ledger
    signature = ledger.sign(txn.get_sign_message())
    tx_raw_bytes = txn.get_tx_data(signature, public_key, tx_sign.SIGN_MODE_LEGACY_AMINO_JSON)

    # Broadcast the transaction
    tx_block = c.send_tx_block_mode(tx_raw_bytes)

    # Convert to JSON for readability
    print(MessageToJson(tx_block))


if __name__ == "__main__":
    main()
