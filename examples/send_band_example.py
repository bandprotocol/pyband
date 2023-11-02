import asyncio
import os

from pyband import Client, Transaction, Wallet
from pyband.messages.cosmos.bank.v1beta1 import MsgSend
from pyband.proto.cosmos.base.v1beta1 import Coin


async def main():
    # Create a GRPC connection
    grpc_url = "laozi-testnet6.bandchain.org"
    c = Client.from_endpoint(grpc_url, 443)

    # Convert a mnemonic to a wallet
    wallet = Wallet.from_mnemonic(os.getenv("MNEMONIC"))
    sender = wallet.get_address().to_acc_bech32()

    # Prepare a transaction's properties
    msg_send = MsgSend(
        from_address=sender,
        to_address="band19ajhdg6maw0ja0a7qd9sq7nm4ym9f4wjg8r96w",
        amount=[Coin(amount="1000000", denom="uband")],
    )

    account = await c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    chain_id = await c.get_chain_id()

    # Step 4 Construct a transaction
    txn = (
        Transaction()
        .with_messages(msg_send)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas_limit(100000)
        .with_gas_price(0.0025)
        .with_memo("")
    )

    # Sign and broadcast a transaction
    tx_block = await c.send_tx_block_mode(wallet.sign_and_build(txn))

    # Converting to JSON for readability
    print(tx_block.to_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
