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

## Compatible

Band 2.3.0, Cosmos-SDK 0.44.0, IBC-go 1.1.0

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
from pyband.messages.oracle.v1 import MsgRequestData
from pyband.proto.cosmos.base.v1beta1 import Coin


async def main():
    # Create a GRPC connection
    grpc_url = "laozi-testnet6.bandchain.org"
    c = Client.from_endpoint(grpc_url, 443)

    # Convert a mnemonic to a wallet
    wallet = Wallet.from_mnemonic(os.getenv("MNEMONIC"))
    sender = wallet.public_key.to_address().to_acc_bech32()

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

    fee = [Coin(amount="50000", denom="uband")]
    chain_id = await c.get_chain_id()

    # Step 4 Construct a transaction
    txn = (
        Transaction()
        .with_messages(request_msg)
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

Shown below is the expected result after sending the transaction in block mode:

<results>

```json
{
    "height": "43368",
    "txhash": "132F121F6A250FC8A330288DFE3D5C676B75399F9D2CFEF3A00A14CFD15E2B8C",
    "data": "0A1B0A192F6F7261636C652E76312E4D73675265717565737444617461",
    "rawLog": "[{\"events\":[{\"type\":\"coin_received\",\"attributes\":[{\"key\":\"receiver\",\"value\":\"band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec\"},{\"key\":\"amount\",\"value\":\"56uband\"},{\"key\":\"receiver\",\"value\":\"band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec\"},{\"key\":\"amount\",\"value\":\"44uband\"},{\"key\":\"receiver\",\"value\":\"band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec\"},{\"key\":\"amount\",\"value\":\"12uband\"}]},{\"type\":\"coin_spent\",\"attributes\":[{\"key\":\"spender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"amount\",\"value\":\"56uband\"},{\"key\":\"spender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"amount\",\"value\":\"44uband\"},{\"key\":\"spender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"amount\",\"value\":\"12uband\"}]},{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"/oracle.v1.MsgRequestData\"},{\"key\":\"sender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"sender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"sender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"}]},{\"type\":\"raw_request\",\"attributes\":[{\"key\":\"data_source_id\",\"value\":\"276\"},{\"key\":\"data_source_hash\",\"value\":\"7ba8469a301269860fcf79323cbf63094350174722457323718fcc98168ddb7e\"},{\"key\":\"external_id\",\"value\":\"6\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"275\"},{\"key\":\"data_source_hash\",\"value\":\"fa899f65777a9f4cacc991dfb8cc834a9a07e1a6d3f0980fb49cc0a2b30ac900\"},{\"key\":\"external_id\",\"value\":\"0\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"277\"},{\"key\":\"data_source_hash\",\"value\":\"cd9209a1ae4967b096ed945c5732bcd1524a791e01fd348cba039eb4d9f2b78b\"},{\"key\":\"external_id\",\"value\":\"3\"},{\"key\":\"calldata\",\"value\":\"BTC\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"273\"},{\"key\":\"data_source_hash\",\"value\":\"1afe5339ca8e6d5e419b3123adabebb2dbdbf58f3613861fdabd72cdf9a199d2\"},{\"key\":\"external_id\",\"value\":\"10\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"271\"},{\"key\":\"data_source_hash\",\"value\":\"e0b968f7c445530735c0d19528c02380f9fe79a9489d354cc25c160d4dfb6e84\"},{\"key\":\"external_id\",\"value\":\"13\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"278\"},{\"key\":\"data_source_hash\",\"value\":\"ffbb4f3d39d216b33b572826f45d5061001d88f7e0a589f2dedd39a9a0403052\"},{\"key\":\"external_id\",\"value\":\"5\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"266\"},{\"key\":\"data_source_hash\",\"value\":\"9bb8f4c66d7f18a91bc37a5dc0455e5259a2d2cd3d82499bf6cfd395776ed2da\"},{\"key\":\"external_id\",\"value\":\"11\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"268\"},{\"key\":\"data_source_hash\",\"value\":\"b1a7c21a999cc196a78f5ea81219054e31e7e06bc2a36005e16a655d66338259\"},{\"key\":\"external_id\",\"value\":\"2\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"270\"},{\"key\":\"data_source_hash\",\"value\":\"4840ef7b0c432687426bbb6d2c99f10b539b2eb7cc3e18e4b96c72171e996fcf\"},{\"key\":\"external_id\",\"value\":\"4\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\",\"value\":\"14uband\"},{\"key\":\"data_source_id\",\"value\":\"267\"},{\"key\":\"data_source_hash\",\"value\":\"e610b043001c217368c284702d99fc04e18e815dbdda0de6658ca5ef7fa6c06f\"},{\"key\":\"external_id\",\"value\":\"9\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"269\"},{\"key\":\"data_source_hash\",\"value\":\"c84973ef3b156483fb8210ee311158aa98fcdfb943ae938992e663fd3bb7b645\"},{\"key\":\"external_id\",\"value\":\"12\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"274\"},{\"key\":\"data_source_hash\",\"value\":\"cfcefcd1627ca8ecd643d1779d98b53806442a97d8e5fff7684e976284f991cb\"},{\"key\":\"external_id\",\"value\":\"7\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\",\"value\":\"11uband\"},{\"key\":\"data_source_id\",\"value\":\"265\"},{\"key\":\"data_source_hash\",\"value\":\"34bd8f6de7a47f232add5e7be00180cf5721e181f624b78a8ae8440e8c64b1bd\"},{\"key\":\"external_id\",\"value\":\"8\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\",\"value\":\"3uband\"},{\"key\":\"data_source_id\",\"value\":\"272\"},{\"key\":\"data_source_hash\",\"value\":\"a1d5671e873f3e84e70e79e82f254fda3f7b012219d5b47eefc1ae2c19dedead\"},{\"key\":\"external_id\",\"value\":\"1\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"}]},{\"type\":\"request\",\"attributes\":[{\"key\":\"id\",\"value\":\"256\"},{\"key\":\"client_id\",\"value\":\"BandProtocol\"},{\"key\":\"oracle_script_id\",\"value\":\"37\"},{\"key\":\"calldata\",\"value\":\"0000000200000003425443000000034554480000000000000064\"},{\"key\":\"ask_count\",\"value\":\"4\"},{\"key\":\"min_count\",\"value\":\"3\"},{\"key\":\"gas_used\",\"value\":\"72720\"},{\"key\":\"total_fees\",\"value\":\"112uband\"},{\"key\":\"validator\",\"value\":\"bandvaloper1njg6cr6gljhhyu59jtrh8e68dmylrdxmv44s4e\"},{\"key\":\"validator\",\"value\":\"bandvaloper1nfxz6dgljkv94etljx5z0myahdsd9gkhm2ydpz\"},{\"key\":\"validator\",\"value\":\"bandvaloper1jkvd20qpvw2wvm6uz5wa67xfgqkeyf9zx7mejg\"},{\"key\":\"validator\",\"value\":\"bandvaloper1p8ukn768xc3unh8ay2pzspzl7ugshfa7wl32vf\"}]},{\"type\":\"transfer\",\"attributes\":[{\"key\":\"recipient\",\"value\":\"band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec\"},{\"key\":\"sender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"amount\",\"value\":\"56uband\"},{\"key\":\"recipient\",\"value\":\"band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec\"},{\"key\":\"sender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"amount\",\"value\":\"44uband\"},{\"key\":\"recipient\",\"value\":\"band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec\"},{\"key\":\"sender\",\"value\":\"band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph\"},{\"key\":\"amount\",\"value\":\"12uband\"}]}]}]",
    "logs": [
        {
            "events": [
                {
                    "type": "coin_received",
                    "attributes": [
                        {
                            "key": "receiver",
                            "value": "band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec"
                        },
                        {
                            "key": "amount",
                            "value": "56uband"
                        },
                        {
                            "key": "receiver",
                            "value": "band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec"
                        },
                        {
                            "key": "amount",
                            "value": "44uband"
                        },
                        {
                            "key": "receiver",
                            "value": "band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec"
                        },
                        {
                            "key": "amount",
                            "value": "12uband"
                        }
                    ]
                },
                {
                    "type": "coin_spent",
                    "attributes": [
                        {
                            "key": "spender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "amount",
                            "value": "56uband"
                        },
                        {
                            "key": "spender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "amount",
                            "value": "44uband"
                        },
                        {
                            "key": "spender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "amount",
                            "value": "12uband"
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "action",
                            "value": "/oracle.v1.MsgRequestData"
                        },
                        {
                            "key": "sender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "sender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "sender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        }
                    ]
                },
                {
                    "type": "raw_request",
                    "attributes": [
                        {
                            "key": "data_source_id",
                            "value": "276"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "7ba8469a301269860fcf79323cbf63094350174722457323718fcc98168ddb7e"
                        },
                        {
                            "key": "external_id",
                            "value": "6"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "275"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "fa899f65777a9f4cacc991dfb8cc834a9a07e1a6d3f0980fb49cc0a2b30ac900"
                        },
                        {
                            "key": "external_id",
                            "value": "0"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "277"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "cd9209a1ae4967b096ed945c5732bcd1524a791e01fd348cba039eb4d9f2b78b"
                        },
                        {
                            "key": "external_id",
                            "value": "3"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "273"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "1afe5339ca8e6d5e419b3123adabebb2dbdbf58f3613861fdabd72cdf9a199d2"
                        },
                        {
                            "key": "external_id",
                            "value": "10"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "271"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "e0b968f7c445530735c0d19528c02380f9fe79a9489d354cc25c160d4dfb6e84"
                        },
                        {
                            "key": "external_id",
                            "value": "13"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "278"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "ffbb4f3d39d216b33b572826f45d5061001d88f7e0a589f2dedd39a9a0403052"
                        },
                        {
                            "key": "external_id",
                            "value": "5"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "266"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "9bb8f4c66d7f18a91bc37a5dc0455e5259a2d2cd3d82499bf6cfd395776ed2da"
                        },
                        {
                            "key": "external_id",
                            "value": "11"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "268"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "b1a7c21a999cc196a78f5ea81219054e31e7e06bc2a36005e16a655d66338259"
                        },
                        {
                            "key": "external_id",
                            "value": "2"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "270"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "4840ef7b0c432687426bbb6d2c99f10b539b2eb7cc3e18e4b96c72171e996fcf"
                        },
                        {
                            "key": "external_id",
                            "value": "4"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee",
                            "value": "14uband"
                        },
                        {
                            "key": "data_source_id",
                            "value": "267"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "e610b043001c217368c284702d99fc04e18e815dbdda0de6658ca5ef7fa6c06f"
                        },
                        {
                            "key": "external_id",
                            "value": "9"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "269"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "c84973ef3b156483fb8210ee311158aa98fcdfb943ae938992e663fd3bb7b645"
                        },
                        {
                            "key": "external_id",
                            "value": "12"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        },
                        {
                            "key": "data_source_id",
                            "value": "274"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "cfcefcd1627ca8ecd643d1779d98b53806442a97d8e5fff7684e976284f991cb"
                        },
                        {
                            "key": "external_id",
                            "value": "7"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee",
                            "value": "11uband"
                        },
                        {
                            "key": "data_source_id",
                            "value": "265"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "34bd8f6de7a47f232add5e7be00180cf5721e181f624b78a8ae8440e8c64b1bd"
                        },
                        {
                            "key": "external_id",
                            "value": "8"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee",
                            "value": "3uband"
                        },
                        {
                            "key": "data_source_id",
                            "value": "272"
                        },
                        {
                            "key": "data_source_hash",
                            "value": "a1d5671e873f3e84e70e79e82f254fda3f7b012219d5b47eefc1ae2c19dedead"
                        },
                        {
                            "key": "external_id",
                            "value": "1"
                        },
                        {
                            "key": "calldata",
                            "value": "BTC ETH"
                        },
                        {
                            "key": "fee"
                        }
                    ]
                },
                {
                    "type": "request",
                    "attributes": [
                        {
                            "key": "id",
                            "value": "256"
                        },
                        {
                            "key": "client_id",
                            "value": "BandProtocol"
                        },
                        {
                            "key": "oracle_script_id",
                            "value": "37"
                        },
                        {
                            "key": "calldata",
                            "value": "0000000200000003425443000000034554480000000000000064"
                        },
                        {
                            "key": "ask_count",
                            "value": "4"
                        },
                        {
                            "key": "min_count",
                            "value": "3"
                        },
                        {
                            "key": "gas_used",
                            "value": "72720"
                        },
                        {
                            "key": "total_fees",
                            "value": "112uband"
                        },
                        {
                            "key": "validator",
                            "value": "bandvaloper1njg6cr6gljhhyu59jtrh8e68dmylrdxmv44s4e"
                        },
                        {
                            "key": "validator",
                            "value": "bandvaloper1nfxz6dgljkv94etljx5z0myahdsd9gkhm2ydpz"
                        },
                        {
                            "key": "validator",
                            "value": "bandvaloper1jkvd20qpvw2wvm6uz5wa67xfgqkeyf9zx7mejg"
                        },
                        {
                            "key": "validator",
                            "value": "bandvaloper1p8ukn768xc3unh8ay2pzspzl7ugshfa7wl32vf"
                        }
                    ]
                },
                {
                    "type": "transfer",
                    "attributes": [
                        {
                            "key": "recipient",
                            "value": "band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec"
                        },
                        {
                            "key": "sender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "amount",
                            "value": "56uband"
                        },
                        {
                            "key": "recipient",
                            "value": "band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec"
                        },
                        {
                            "key": "sender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "amount",
                            "value": "44uband"
                        },
                        {
                            "key": "recipient",
                            "value": "band15vxtygy8ynpw47uk0wq99lsh0e6mywzyc9l4ec"
                        },
                        {
                            "key": "sender",
                            "value": "band18p27yl962l8283ct7srr5l3g7ydazj07dqrwph"
                        },
                        {
                            "key": "amount",
                            "value": "12uband"
                        }
                    ]
                }
            ]
        }
    ],
    "gasWanted": "2000000",
    "gasUsed": "487065",
    "events": [
        {
            "type": "tx",
            "attributes": [
                {
                    "key": "ZmVl",
                    "value": "MHViYW5k",
                    "index": true
                }
            ]
        },
        {
            "type": "tx",
            "attributes": [
                {
                    "key": "YWNjX3NlcQ==",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaC8z",
                    "index": true
                }
            ]
        },
        {
            "type": "tx",
            "attributes": [
                {
                    "key": "c2lnbmF0dXJl",
                    "value": "SFkrcmZ0SVRycGEvZHZKa1dydEtCaTRVTi9mcC94Y3dNaTlZZ3dFdDcwOWo3c0lGSjE0ODlKaHcvdGlDR2RFek52WlRoYmxsUHh3Rk1vVGFNZmpZVVE9PQ==",
                    "index": true
                }
            ]
        },
        {
            "type": "message",
            "attributes": [
                {
                    "key": "YWN0aW9u",
                    "value": "L29yYWNsZS52MS5Nc2dSZXF1ZXN0RGF0YQ==",
                    "index": true
                }
            ]
        },
        {
            "type": "coin_spent",
            "attributes": [
                {
                    "key": "c3BlbmRlcg==",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "NTZ1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "coin_received",
            "attributes": [
                {
                    "key": "cmVjZWl2ZXI=",
                    "value": "YmFuZDE1dnh0eWd5OHlucHc0N3VrMHdxOTlsc2gwZTZteXd6eWM5bDRlYw==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "NTZ1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "transfer",
            "attributes": [
                {
                    "key": "cmVjaXBpZW50",
                    "value": "YmFuZDE1dnh0eWd5OHlucHc0N3VrMHdxOTlsc2gwZTZteXd6eWM5bDRlYw==",
                    "index": true
                },
                {
                    "key": "c2VuZGVy",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "NTZ1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "message",
            "attributes": [
                {
                    "key": "c2VuZGVy",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                }
            ]
        },
        {
            "type": "coin_spent",
            "attributes": [
                {
                    "key": "c3BlbmRlcg==",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "NDR1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "coin_received",
            "attributes": [
                {
                    "key": "cmVjZWl2ZXI=",
                    "value": "YmFuZDE1dnh0eWd5OHlucHc0N3VrMHdxOTlsc2gwZTZteXd6eWM5bDRlYw==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "NDR1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "transfer",
            "attributes": [
                {
                    "key": "cmVjaXBpZW50",
                    "value": "YmFuZDE1dnh0eWd5OHlucHc0N3VrMHdxOTlsc2gwZTZteXd6eWM5bDRlYw==",
                    "index": true
                },
                {
                    "key": "c2VuZGVy",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "NDR1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "message",
            "attributes": [
                {
                    "key": "c2VuZGVy",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                }
            ]
        },
        {
            "type": "coin_spent",
            "attributes": [
                {
                    "key": "c3BlbmRlcg==",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "MTJ1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "coin_received",
            "attributes": [
                {
                    "key": "cmVjZWl2ZXI=",
                    "value": "YmFuZDE1dnh0eWd5OHlucHc0N3VrMHdxOTlsc2gwZTZteXd6eWM5bDRlYw==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "MTJ1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "transfer",
            "attributes": [
                {
                    "key": "cmVjaXBpZW50",
                    "value": "YmFuZDE1dnh0eWd5OHlucHc0N3VrMHdxOTlsc2gwZTZteXd6eWM5bDRlYw==",
                    "index": true
                },
                {
                    "key": "c2VuZGVy",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                },
                {
                    "key": "YW1vdW50",
                    "value": "MTJ1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "message",
            "attributes": [
                {
                    "key": "c2VuZGVy",
                    "value": "YmFuZDE4cDI3eWw5NjJsODI4M2N0N3NycjVsM2c3eWRhemowN2RxcndwaA==",
                    "index": true
                }
            ]
        },
        {
            "type": "request",
            "attributes": [
                {
                    "key": "aWQ=",
                    "value": "MjU2",
                    "index": true
                },
                {
                    "key": "Y2xpZW50X2lk",
                    "value": "QmFuZFByb3RvY29s",
                    "index": true
                },
                {
                    "key": "b3JhY2xlX3NjcmlwdF9pZA==",
                    "value": "Mzc=",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "MDAwMDAwMDIwMDAwMDAwMzQyNTQ0MzAwMDAwMDAzNDU1NDQ4MDAwMDAwMDAwMDAwMDA2NA==",
                    "index": true
                },
                {
                    "key": "YXNrX2NvdW50",
                    "value": "NA==",
                    "index": true
                },
                {
                    "key": "bWluX2NvdW50",
                    "value": "Mw==",
                    "index": true
                },
                {
                    "key": "Z2FzX3VzZWQ=",
                    "value": "NzI3MjA=",
                    "index": true
                },
                {
                    "key": "dG90YWxfZmVlcw==",
                    "value": "MTEydWJhbmQ=",
                    "index": true
                },
                {
                    "key": "dmFsaWRhdG9y",
                    "value": "YmFuZHZhbG9wZXIxbmpnNmNyNmdsamhoeXU1OWp0cmg4ZTY4ZG15bHJkeG12NDRzNGU=",
                    "index": true
                },
                {
                    "key": "dmFsaWRhdG9y",
                    "value": "YmFuZHZhbG9wZXIxbmZ4ejZkZ2xqa3Y5NGV0bGp4NXowbXlhaGRzZDlna2htMnlkcHo=",
                    "index": true
                },
                {
                    "key": "dmFsaWRhdG9y",
                    "value": "YmFuZHZhbG9wZXIxamt2ZDIwcXB2dzJ3dm02dXo1d2E2N3hmZ3FrZXlmOXp4N21lamc=",
                    "index": true
                },
                {
                    "key": "dmFsaWRhdG9y",
                    "value": "YmFuZHZhbG9wZXIxcDh1a243Njh4YzN1bmg4YXkycHpzcHpsN3Vnc2hmYTd3bDMydmY=",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjc2",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "N2JhODQ2OWEzMDEyNjk4NjBmY2Y3OTMyM2NiZjYzMDk0MzUwMTc0NzIyNDU3MzIzNzE4ZmNjOTgxNjhkZGI3ZQ==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "Ng==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjc1",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "ZmE4OTlmNjU3NzdhOWY0Y2FjYzk5MWRmYjhjYzgzNGE5YTA3ZTFhNmQzZjA5ODBmYjQ5Y2MwYTJiMzBhYzkwMA==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "MA==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjc3",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "Y2Q5MjA5YTFhZTQ5NjdiMDk2ZWQ5NDVjNTczMmJjZDE1MjRhNzkxZTAxZmQzNDhjYmEwMzllYjRkOWYyYjc4Yg==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "Mw==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRD",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjcz",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "MWFmZTUzMzljYThlNmQ1ZTQxOWIzMTIzYWRhYmViYjJkYmRiZjU4ZjM2MTM4NjFmZGFiZDcyY2RmOWExOTlkMg==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "MTA=",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjcx",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "ZTBiOTY4ZjdjNDQ1NTMwNzM1YzBkMTk1MjhjMDIzODBmOWZlNzlhOTQ4OWQzNTRjYzI1YzE2MGQ0ZGZiNmU4NA==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "MTM=",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjc4",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "ZmZiYjRmM2QzOWQyMTZiMzNiNTcyODI2ZjQ1ZDUwNjEwMDFkODhmN2UwYTU4OWYyZGVkZDM5YTlhMDQwMzA1Mg==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "NQ==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "MjY2",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "OWJiOGY0YzY2ZDdmMThhOTFiYzM3YTVkYzA0NTVlNTI1OWEyZDJjZDNkODI0OTliZjZjZmQzOTU3NzZlZDJkYQ==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "MTE=",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "MjY4",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "YjFhN2MyMWE5OTljYzE5NmE3OGY1ZWE4MTIxOTA1NGUzMWU3ZTA2YmMyYTM2MDA1ZTE2YTY1NWQ2NjMzODI1OQ==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "Mg==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjcw",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "NDg0MGVmN2IwYzQzMjY4NzQyNmJiYjZkMmM5OWYxMGI1MzliMmViN2NjM2UxOGU0Yjk2YzcyMTcxZTk5NmZjZg==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "NA==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "value": "MTR1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "MjY3",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "ZTYxMGIwNDMwMDFjMjE3MzY4YzI4NDcwMmQ5OWZjMDRlMThlODE1ZGJkZGEwZGU2NjU4Y2E1ZWY3ZmE2YzA2Zg==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "OQ==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "MjY5",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "Yzg0OTczZWYzYjE1NjQ4M2ZiODIxMGVlMzExMTU4YWE5OGZjZGZiOTQzYWU5Mzg5OTJlNjYzZmQzYmI3YjY0NQ==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "MTI=",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjc0",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "Y2ZjZWZjZDE2MjdjYThlY2Q2NDNkMTc3OWQ5OGI1MzgwNjQ0MmE5N2Q4ZTVmZmY3Njg0ZTk3NjI4NGY5OTFjYg==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "Nw==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "value": "MTF1YmFuZA==",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "MjY1",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "MzRiZDhmNmRlN2E0N2YyMzJhZGQ1ZTdiZTAwMTgwY2Y1NzIxZTE4MWY2MjRiNzhhOGFlODQ0MGU4YzY0YjFiZA==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "OA==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "value": "M3ViYW5k",
                    "index": true
                }
            ]
        },
        {
            "type": "raw_request",
            "attributes": [
                {
                    "key": "ZGF0YV9zb3VyY2VfaWQ=",
                    "value": "Mjcy",
                    "index": true
                },
                {
                    "key": "ZGF0YV9zb3VyY2VfaGFzaA==",
                    "value": "YTFkNTY3MWU4NzNmM2U4NGU3MGU3OWU4MmYyNTRmZGEzZjdiMDEyMjE5ZDViNDdlZWZjMWFlMmMxOWRlZGVhZA==",
                    "index": true
                },
                {
                    "key": "ZXh0ZXJuYWxfaWQ=",
                    "value": "MQ==",
                    "index": true
                },
                {
                    "key": "Y2FsbGRhdGE=",
                    "value": "QlRDIEVUSA==",
                    "index": true
                },
                {
                    "key": "ZmVl",
                    "index": true
                }
            ]
        }
    ]
}
```

</results>

## 🧀 Notes

For more examples, please go to [`examples`](/examples/request_data_example.py).
