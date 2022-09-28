import asyncio

from pyband import Client, Transaction
from pyband.messages.oracle.v1 import MsgEditDataSource
from pyband.proto.cosmos.base.v1beta1 import Coin
from pyband.proto.cosmos.tx.signing.v1beta1 import SignMode
from pyband.wallet import Ledger


def main():
    # Create the gRPC connection
    grpc_url = "laozi-testnet5.bandchain.org"
    c = Client.from_endpoint(grpc_url, 443)

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

    account = await c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    fee = [Coin(amount="0", denom="uband")]
    chain_id = await c.get_chain_id()

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
    signature = ledger.sign(txn.get_sign_message_for_legacy_codec())
    tx_raw_bytes = txn.get_tx_data(signature, public_key, SignMode.SIGN_MODE_LEGACY_AMINO_JSON)

    # Broadcast the transaction
    tx_block = await c.send_tx_block_mode(tx_raw_bytes)

    # Convert to JSON for readability
    print(tx_block.to_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
