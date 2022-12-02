import asyncio
import os

from pyband import Client, Transaction, Wallet
from pyband.messages.oracle.v1 import MsgRequestData
from pyband.proto.cosmos.base.v1beta1 import Coin


async def main():
    # Create a GRPC connection
    grpc_url = "laozi-testnet6.bandchain.org"
    c = Client.from_endpoint(grpc_url, 443)

    # Convert a mnemonic to a wallet
    wallet = Wallet.from_mnemonic(os.getenv("MNEMONIC"))
    sender = wallet.get_address().to_acc_bech32()

    # Prepare a transaction's properties
    request_msg = MsgRequestData(
        oracle_script_id=37,
        calldata=bytes.fromhex("0000000200000003425443000000034554480000000000000064"),
        ask_count=4,
        min_count=3,
        client_id="BandProtocol",
        fee_limit=[Coin(amount="112", denom="uband")],
        prepare_gas=50000,
        execute_gas=200000,
        sender=sender,
    )

    account = await c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    chain_id = await c.get_chain_id()

    # Step 4 Construct a transaction
    txn = (
        Transaction()
        .with_messages(request_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas_limit(650000)
        .with_gas_price(0.0025)
        .with_memo("")
    )

    # Sign and broadcast a transaction
    tx_block = await c.send_tx_block_mode(wallet.sign_and_build(txn))

    # Converting to JSON for readability
    print(tx_block.to_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
