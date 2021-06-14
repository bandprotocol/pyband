import grpc
from pyband.client import Client
from pyband.transaction import Transaction

from pyband.data import HexBytes
from pyband.wallet import PrivateKey
from pyband.obi import PyObi

from pyband.proto.oracle.v1 import tx_pb2 as tx_oracle
from pyband.proto.cosmos.base.v1beta1 import coin_pb2 as coin_type
from pyband.proto.cosmos.tx.v1beta1 import tx_pb2 as cosmos_tx_type

def main():
    # Running LocalHost
    # c = Cli('localhost:9090')
    c = Client("rpc-laozi-testnet1.bandchain.org:9090")
    CHAIN_ID = c.get_chain_id()
    MNEMONIC = "foo"
    private_key = PrivateKey.from_mnemonic(MNEMONIC)
    public_key = private_key.to_pubkey()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()
    obi = PyObi("{symbols:[string],multiplier:u64}/{rates:[u64]}")
    calldata = obi.encode({"symbols": ["ETH", "BTC", "BAND", "MIR", "UNI"], "multiplier": 100})

    msg = tx_oracle.MsgRequestData(
        oracle_script_id=37,
        calldata=calldata,
        ask_count=16,
        min_count=10,
        client_id="Blue",
        fee_limit=[],
        prepare_gas=200000,
        execute_gas=2000000,
        sender=sender,
    )
    account = c.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence
    fee = cosmos_tx_type.Fee(amount=[coin_type.Coin(amount="1000000", denom="uband")], gas_limit=2000000)

    txn = (
        Transaction()
        .with_messages(msg)
        .with_account_num(account_num)
        .with_sequence(sequence)
        .with_chain_id(CHAIN_ID)
        .with_gas(20000)
        .with_fee(fee)
    )

    tx_raw_bytes = txn.get_tx_data(private_key)
    t_send_tx_sync_mode(c, tx_raw_bytes)

def t_get_data_source(c, id=1):
    print("------------- get_data_source----------------")
    print(c.get_data_source(id=1))


def t_get_oracle_script(c, id=1):
    print("------------- get_oracle_script----------------")
    print(c.get_oracle_script(id=1))


def t_get_request_by_id(c, id=1):
    print("------------- get_request_by_id----------------")
    print(c.get_request_by_id(id))


def t_get_latest_block(c):
    print("------------- get_latest_block----------------")
    print(c.get_latest_block())


def t_get_reporters(c, validator="bandvaloper18tjynh8v0kvf9lmjenx02fgltxk0c6jmm2wcjc"):
    print("------------- get_reporters----------------")
    print(c.get_reporters(validator))


def t_get_request_id_by_tx_hash(c, id="AFC6BDDC7E7041B1AC21C26E25A52550689D148BE9A0D8E797E45DD753BF7FB3"):
    print("------------- get_request_id_by_tx_hash---------------")
    print(c.get_request_id_by_tx_hash(HexBytes(id)))


def t_get_account(c, addr="band1ee656yzw6y9swqayu9v0kgu5pua2kgjq3hd6g3"):
    print("------------- get_account---------------")
    print(c.get_account(addr))


def t_send_tx_sync_mode(c, tx_byte):
    print("-------------send_tx_sync_mode---------------")
    print(c.send_tx_sync_mode(tx_byte))


def t_send_tx_async_mode(c, tx_byte):
    print("------------- send_tx_async_mode---------------")
    print(c.send_tx_async_mode(tx_byte))


def t_send_tx_block_mode(c, tx_byte):
    print("------------- send_tx_block_mode---------------")
    print(c.send_tx_block_mode(tx_byte))


if __name__ == "__main__":
    main()
