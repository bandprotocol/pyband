<div align="center">
    <h2>PyBand</h2>
    <blockquote>BandChain Python Library</blockquote>
</div>

Pyband is a library that is used for interacting with BandChain using `gRPC` protocol. Querying data and sending transaction can be done here!

## ⭐️ Features

This helper library allows users to interact with Bandchain where the following features can be done easily.

- Getting information of a specific oracle script, data source, and request ID.
- Getting the account information of the specify address
- Getting the latest request of the oracle script ID that matches the data and number of validators required to complete the job.
- Getting reference data of pairs of data.
- Seeing all the reporters associated with the specify validator.
- Seeing what Bandchain you are using and getting the latest block in Bandchain.
- Sending transaction in 3 modes, including block mode, async mode, and sync mode.

## 📦 Installation

The library is available on [PyPI](https://pypi.org/project/pyband/)

```bash
pip install pyband
```

## Compatible

Band 2.3.0, Cosmos-SDK 0.44.0, IBC-go 1.1.0


## 💎 Example Usage

The example code below shows how the library can be used to get the result of the latest request for the price of any cryptocurrency. In this example, we will get the latest price of the following coin - BTC, ETH, MIR, ANC, DOGE, and LUNA. The specified parameters are

- `oracleScriptID`: 37
- `calldata`: The hex string representing [OBI](<https://github.com/bandprotocol/bandchain/wiki/Oracle-Binary-Encoding-(OBI)>)-encoded value of `{'symbols': ['BTC', 'ETH', 'MIR', 'ANC', 'DOGE', 'LUNA'], 'multiplier': 1000000000}`
- `minCount`: 3
- `askCount`: 6

```python
from pyband import Client, PyObi


def main():
    grpc_url = "rpc-laozi-testnet2.bandchain.org:9090"
    c = Client(grpc_url, insecure=True)

    oid = 37
    calldata = "000000060000000342544300000003455448000000034d495200000003414e4300000004444f4745000000044c554e41000000003b9aca00"
    min_count = 3
    ask_count = 6

    req_info = c.get_latest_request(oid, calldata, min_count, ask_count)
    oracle_script = c.get_oracle_script(oid)
    obi = PyObi(oracle_script.schema)

    # Convert the calldata to readable syntax
    print(obi.decode_input(bytes.fromhex(calldata)))

    # Showing the result
    print(obi.decode_output(req_info.request.result.result))

if __name__ == "__main__":
    main()
```

Here is the result of the program above.

```
{'symbols': ['BTC', 'ETH', 'MIR', 'ANC', 'DOGE', 'LUNA'], 'multiplier': 1000000000}
{'rates': [31966219600000, 1891714500000, 3280000000, 2012829000, 190938000, 7080000000]}
```

Another example shows how to send a transaction to Bandchain using block mode.

```python
import os

from pyband import Client, Transaction, PrivateKey

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.oracle.v1.tx_pb2 import MsgRequestData
from google.protobuf.json_format import MessageToJson


def main():
    # Step 1 Create a gRPC connection
    grpc_url = "rpc-laozi-testnet2.bandchain.org:9090"
    c = Client(grpc_url)

    # Step 2 Convert a menmonic to private key, public key, and sender
    MNEMONIC = os.getenv("MNEMONIC")
    private_key = PrivateKey.from_mnemonic(MNEMONIC)
    public_key = private_key.to_public_key()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()

    # Step 3 Prepare a transaction's properties
    request_msg = MsgRequestData(
        oracle_script_id=37,
        calldata=bytes.fromhex("0000000200000003425443000000034554480000000000000064"),
        ask_count=4,
        min_count=3,
        client_id="BandProtocol",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=50000,
        execute_gas=200000,
        sender=sender,
    )

    account = c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    fee = [Coin(amount="0", denom="uband")]
    chain_id = c.get_chain_id()

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

    # Step 5 Sign a transaction by using private key
    sign_doc = txn.get_sign_doc(public_key)
    signature = private_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = txn.get_tx_data(signature, public_key)

    # Step 6 Broadcast a transaction
    tx_block = c.send_tx_block_mode(tx_raw_bytes)

    # Converting to JSON for readability
    print(MessageToJson(tx_block))

if __name__ == "__main__":
    main()
```

Here is the result after sending a block transaction

```
{"height":"1136536","txhash":"9B854B9A36A1BFFE3BF16E75E9E8BE2FF5A5D5E4700D17492F3317809527178D","data":"0A090A0772657175657374","rawLog":"[{\"events\":[{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"request\"}]},{\"type\":\"raw_request\",\"attributes\":[{\"key\":\"data_source_id\",\"value\":\"61\"},{\"key\":\"data_source_hash\",\"value\":\"07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef\"},{\"key\":\"external_id\",\"value\":\"6\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"57\"},{\"key\":\"data_source_hash\",\"value\":\"61b369daa5c0918020a52165f6c7662d5b9c1eee915025cb3d2b9947a26e48c7\"},{\"key\":\"external_id\",\"value\":\"0\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"62\"},{\"key\":\"data_source_hash\",\"value\":\"107048da9dbf7960c79fb20e0585e080bb9be07d42a1ce09c5479bbada8d0289\"},{\"key\":\"external_id\",\"value\":\"3\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"60\"},{\"key\":\"data_source_hash\",\"value\":\"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac\"},{\"key\":\"external_id\",\"value\":\"5\"},{\"key\":\"calldata\",\"value\":\"huobipro BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"59\"},{\"key\":\"data_source_hash\",\"value\":\"5c011454981c473af3bf6ef93c76b36bfb6cc0ce5310a70a1ba569de3fc0c15d\"},{\"key\":\"external_id\",\"value\":\"2\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"60\"},{\"key\":\"data_source_hash\",\"value\":\"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac\"},{\"key\":\"external_id\",\"value\":\"4\"},{\"key\":\"calldata\",\"value\":\"binance BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"60\"},{\"key\":\"data_source_hash\",\"value\":\"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac\"},{\"key\":\"external_id\",\"value\":\"9\"},{\"key\":\"calldata\",\"value\":\"bittrex BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"60\"},{\"key\":\"data_source_hash\",\"value\":\"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac\"},{\"key\":\"external_id\",\"value\":\"7\"},{\"key\":\"calldata\",\"value\":\"kraken BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"60\"},{\"key\":\"data_source_hash\",\"value\":\"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac\"},{\"key\":\"external_id\",\"value\":\"8\"},{\"key\":\"calldata\",\"value\":\"bitfinex BTC ETH\"},{\"key\":\"fee\"},{\"key\":\"data_source_id\",\"value\":\"58\"},{\"key\":\"data_source_hash\",\"value\":\"7e6759fade717a06fb643392bfde837bfc3437da2ded54feed706e6cd35de461\"},{\"key\":\"external_id\",\"value\":\"1\"},{\"key\":\"calldata\",\"value\":\"BTC ETH\"},{\"key\":\"fee\"}]},{\"type\":\"request\",\"attributes\":[{\"key\":\"id\",\"value\":\"916006\"},{\"key\":\"client_id\",\"value\":\"BandProtocol\"},{\"key\":\"oracle_script_id\",\"value\":\"37\"},{\"key\":\"calldata\",\"value\":\"0000000200000003425443000000034554480000000000000064\"},{\"key\":\"ask_count\",\"value\":\"4\"},{\"key\":\"min_count\",\"value\":\"3\"},{\"key\":\"gas_used\",\"value\":\"111048\"},{\"key\":\"total_fees\"},{\"key\":\"validator\",\"value\":\"bandvaloper1e9sa38742tzhmandc4gkqve9zy8zc0yremaa3j\"},{\"key\":\"validator\",\"value\":\"bandvaloper19eu9g3gka6rxlevkjlvjq7s6c498tejnwxjwxx\"},{\"key\":\"validator\",\"value\":\"bandvaloper17n5rmujk78nkgss7tjecg4nfzn6geg4cqtyg3u\"},{\"key\":\"validator\",\"value\":\"bandvaloper1zl5925n5u24njn9axpygz8lhjl5a8v4cpkzx5g\"}]}]}]","logs":[{"events":[{"type":"message","attributes":[{"key":"action","value":"request"}]},{"type":"raw_request","attributes":[{"key":"data_source_id","value":"61"},{"key":"data_source_hash","value":"07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef"},{"key":"external_id","value":"6"},{"key":"calldata","value":"BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"57"},{"key":"data_source_hash","value":"61b369daa5c0918020a52165f6c7662d5b9c1eee915025cb3d2b9947a26e48c7"},{"key":"external_id","value":"0"},{"key":"calldata","value":"BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"62"},{"key":"data_source_hash","value":"107048da9dbf7960c79fb20e0585e080bb9be07d42a1ce09c5479bbada8d0289"},{"key":"external_id","value":"3"},{"key":"calldata","value":"BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"5"},{"key":"calldata","value":"huobipro BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"59"},{"key":"data_source_hash","value":"5c011454981c473af3bf6ef93c76b36bfb6cc0ce5310a70a1ba569de3fc0c15d"},{"key":"external_id","value":"2"},{"key":"calldata","value":"BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"4"},{"key":"calldata","value":"binance BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"9"},{"key":"calldata","value":"bittrex BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"7"},{"key":"calldata","value":"kraken BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"8"},{"key":"calldata","value":"bitfinex BTC ETH"},{"key":"fee"},{"key":"data_source_id","value":"58"},{"key":"data_source_hash","value":"7e6759fade717a06fb643392bfde837bfc3437da2ded54feed706e6cd35de461"},{"key":"external_id","value":"1"},{"key":"calldata","value":"BTC ETH"},{"key":"fee"}]},{"type":"request","attributes":[{"key":"id","value":"916006"},{"key":"client_id","value":"BandProtocol"},{"key":"oracle_script_id","value":"37"},{"key":"calldata","value":"0000000200000003425443000000034554480000000000000064"},{"key":"ask_count","value":"4"},{"key":"min_count","value":"3"},{"key":"gas_used","value":"111048"},{"key":"total_fees"},{"key":"validator","value":"bandvaloper1e9sa38742tzhmandc4gkqve9zy8zc0yremaa3j"},{"key":"validator","value":"bandvaloper19eu9g3gka6rxlevkjlvjq7s6c498tejnwxjwxx"},{"key":"validator","value":"bandvaloper17n5rmujk78nkgss7tjecg4nfzn6geg4cqtyg3u"},{"key":"validator","value":"bandvaloper1zl5925n5u24njn9axpygz8lhjl5a8v4cpkzx5g"}]}]}],"gasWanted":"2000000","gasUsed":"564187"}
```

## 🧀 Notes

For more examples, please see [`example`](/example.py) file by running a command `python example.py`.
