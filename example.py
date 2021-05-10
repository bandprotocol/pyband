from pyband.wallet import Address
from pyband import Client, PyObi, PrivateKey


def main():
    # TODO
    c = Client("http://35.187.228.10:1317")
    # req_info = c.get_latest_request(6, bytes.fromhex("000000045041584700000003555344000000003b9aca00"), 4, 4)
    # oracle_script = c.get_oracle_script(6)
    # obi = PyObi(oracle_script.schema)
    # print(obi.decode_output(req_info.result.response_packet_data.result))

    _, priv = PrivateKey.generate()
    addr = priv.to_pubkey().to_address()
    print(addr.to_acc_bech32())
    # print(priv.to_pubkey().to_acc_bech32(), priv.to_pubkey().to_address().to_acc_bech32())

    print(c.get_account(Address.from_acc_bech32("band1p40yh3zkmhcv0ecqp3mcazy83sa57rgjp07dun")))
    # print(c.get_data_source(1))
    # print(c.get_request_by_id(1))

    # print(c.get_reference_data(["ETH/USD", "BTC/ETH", "BAND/BTC"], 2, 4))


if __name__ == "__main__":
    main()
