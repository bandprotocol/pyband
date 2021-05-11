import os
from dotenv import load_dotenv
from pyband.data import Coin
from pyband.wallet import Address
from pyband import Client, PyObi, PrivateKey
from pyband.transaction import Transaction
from pyband.message import MsgRequest, MsgSend


def main():
    # TODO
    load_dotenv()
    c = Client("http://35.187.228.10:1317")
    # req_info = c.get_latest_request(6, bytes.fromhex("000000045041584700000003555344000000003b9aca00"), 4, 4)
    # oracle_script = c.get_oracle_script(6)
    # obi = PyObi(oracle_script.schema)
    # print(obi.decode_output(req_info.result.response_packet_data.result))

    # _, priv = PrivateKey.generate()
    priv = PrivateKey.from_mnemonic(os.getenv("TEST_MNEMONIC"))
    addr = priv.to_pubkey().to_address()
    # print(addr.to_acc_bech32())

    pubkey = priv.to_pubkey()
    account = c.get_account(addr)
    chain_id = "bandchain"

    # Step 3
    t = (
        Transaction()
        .with_messages(
            # MsgSend(
            #     from_address=addr,
            #     to_address=Address.from_acc_bech32("band1jrhuqrymzt4mnvgw8cvy3s9zhx3jj0dq30qpte"),
            #     amount=[Coin(amount=9999, denom="uband")],
            # )
            MsgRequest(
                oracle_script_id=1,
                calldata=bytes.fromhex("0000000342544300000000000003e8"),
                ask_count=2,
                min_count=1,
                client_id="from_pyband",
                fee_limit=[Coin(amount=1000000, denom="uband")],
                prepare_gas=50000,
                execute_gas=300000,
                sender=addr,
            ),
        )
        .with_account_num(account.account_number)
        .with_sequence(account.sequence)
        .with_chain_id(chain_id)
        .with_gas(1000000)
        .with_memo("TEST")
    )

    # Step 4
    raw_data = t.get_sign_data()
    signature = priv.sign(raw_data)
    raw_tx = t.get_tx_data(signature, pubkey)

    print(c.send_tx_block_mode(raw_tx))

    # print(priv.to_pubkey().to_acc_bech32(), priv.to_pubkey().to_address().to_acc_bech32())

    # print(c.get_account(Address.from_acc_bech32("band1p40yh3zkmhcv0ecqp3mcazy83sa57rgjp07dun")))
    # print(c.get_data_source(1))
    # print(c.get_request_by_id(1))

    # print(c.get_reference_data(["ETH/USD", "BTC/ETH", "BAND/BTC"], 2, 4))


if __name__ == "__main__":
    main()
