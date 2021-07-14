<div align="center">
  <h2>PyBand</h2>
  <blockquote>BandChain Python Library</blockquote>
</div>

Pyband is a library that is used for interacting with BandChain using `gRPC` protocol.

## ⭐️ Features

This helper library allows users to request the latest request result that match certain input parameters. The parameters that can be specified are:

-   The `oracleScriptID`
-   the `askCount` and `minCount`
-   the `calldata` (request parameters) associated with the request

For more information on each these, please refer to our [wiki](https://github.com/bandprotocol/bandchain/wiki/Protocol-Messages#parameters-4).

## 📦 Installation

The library is available on [PyPI](https://pypi.org/project/pyband/)

```bash
pip install pyband
```

## 💎 Example Usage

The example code below shows how the library can be used to get the result of the latest request for the price of any cryptocurrency. In this example, we will get the latest price of the following coin - BTC, ETH, MIR, ANC, DOGE, and LUNA. The specified parameters are

-   `oracleScriptID`: 37
-   `calldata`: The hex string representing [OBI](<https://github.com/bandprotocol/bandchain/wiki/Oracle-Binary-Encoding-(OBI)>)-encoded value of `{'symbols': ['BTC', 'ETH', 'MIR', 'ANC', 'DOGE', 'LUNA'], 'multiplier': 1000000000}`
-   `minCount`: 3
-   `askCount`: 6

```python
from pyband import Client, PyObi


def main():
  grpc_url = "rpc-laozi-testnet2.bandchain.org:9090"
  c = Client(grpc_url)

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

Here is the result of the program above
```
{'symbols': ['BTC', 'ETH', 'MIR', 'ANC', 'DOGE', 'LUNA'], 'multiplier': 1000000000}
{'rates': [31966219600000, 1891714500000, 3280000000, 2012829000, 190938000, 7080000000]}
```

## 🧀 Notes
For more examples, please see [`example`](/example.py) file by running a command `python example.py`. For further information, please look at our official [doc](https://pyband-preview-doc.surge.sh/client-library/pyband/get-started.html).
