<div align="center">
    <h2>PyBand</h2>
    <blockquote>BandChain Python Library</blockquote>
</div>

Pyband is a library that is used to interact with BandChain through the `gRPC` protocol. Querying data and sending
transaction can be done here!

## ⭐️ Features

This helper library allows users to interact with BandChain.

PyBand supports the following features:

- Getting the information of a specific oracle script, data source, and request ID.
- Getting the account information of specific address.
- Getting the latest request for a specific oracle script with its matching calldata and validator ask_count and
  min_count.
- Querying all the reporters associated with a specific validator.
- Seeing what client_id you are using and getting BandChain's latest block data.
- Able to send transaction in 3 modes: block mode, async mode, and sync mode.

## 📦 Installation

This library is available on [PyPI](https://pypi.org/project/pyband/)

```bash
pip install pyband
```

## 💎 Example Usage

The example below shows how this library can be used to get the result of the latest request for the price of any
cryptocurrency. In this example, we will get the latest price of BTC on BandChain's testnet.

The specified parameters are:

- `oracleScriptID`: 111
- `calldata`: The hex string representing the [OBI](<https://github.com/bandprotocol/bandchain/wiki/Oracle-Binary-Encoding-(OBI)>)-encoded value of `{'symbols': ['BTC'], 'multiplier': 100000000}`
- `minCount`: 10
- `askCount`: 16

```python
import asyncio

from pyband import Client, PyObi


async def main():
    grpc_url = "laozi-testnet6.bandchain.org"
    c = Client.from_endpoint(grpc_url, 443)

    oid = 111
    calldata = "00000001000000034254430000000005f5e100"
    min_count = 10
    ask_count = 16

    req_info = await c.get_latest_request(oid, calldata, min_count, ask_count)
    oracle_script = await c.get_oracle_script(oid)
    obi = PyObi(oracle_script.schema)

    # Converts the calldata into a readable syntax
    print(obi.decode_input(bytes.fromhex(calldata)))

    # Prints the result
    print(obi.decode_output(req_info.request.result.result))


if __name__ == "__main__":
    asyncio.run(main())
```

Below is the results of the example above.

```
{'symbols': ['BTC'], 'multiplier': 100000000}
{'rates': [1936488410000]}
```

This example shows how to send a transaction on BandChain using block mode.

```python
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

    fee = [Coin(amount="50000", denom="uband")]
    chain_id = await c.get_chain_id()

    # Step 4 Construct a transaction
    txn = (
        Transaction()
        .with_messages(msg_send)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas(2000000)
        .with_fee(fee)
        .with_memo("")
    )

    # Sign and broadcast a transaction
    tx_block = await c.send_tx_block_mode(wallet.sign_and_build(txn))

    # Converting to JSON for readability
    print(tx_block.to_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
```

## 🧀 Notes

For more examples, please go to [`examples`](/examples/request_data_example.py).
