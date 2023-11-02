import asyncio

from pyband import Client, Transaction, Wallet
from pyband.messages.oracle.v1 import MsgEditDataSource
from pyband.proto.cosmos.base.v1beta1 import Coin


async def main():
    # Create the gRPC connection
    grpc_url = "laozi-testnet6.bandchain.org"
    c = Client.from_endpoint(grpc_url, 443)

    # Get the public key and sender from the ledger
    wallet = Wallet.from_ledger()
    sender = wallet.get_address().to_acc_bech32()

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

    chain_id = await c.get_chain_id()

    # Construct the transaction
    txn = (
        Transaction()
        .with_messages(edit_ds_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas_limit(200000)
        .with_gas_price(0.0025)
    )

    # Sign and broadcast a transaction
    tx_block = await c.send_tx_block_mode(wallet.sign_and_build(txn))

    # Convert to JSON for readability
    print(tx_block.to_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
