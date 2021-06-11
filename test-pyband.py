import grpc
from pyband.client2 import Cli
from pyband.transaction2 import Trans

from pyband.data import HexBytes
from pyband.wallet import PrivateKey
from pyband.message import MsgRequest
from pyband.obi import PyObi
from pyband.transaction import Transaction

from pyband.cosmos.crypto.ed25519 import keys_pb2
from pyband.oracle.v1 import tx_pb2_grpc as tx_grpc
from pyband.oracle.v1 import tx_pb2 as tx_oracle


def main():
    # Running LocalHost
    # c = Cli('localhost:9090')
    c = Cli("rpc-laozi-testnet1.bandchain.org:9090")
    CHAIN_ID = "band-laozi-testnet1"  # Should use get_chain_id
    MNEMONIC = "foo"
    private_key = PrivateKey.from_mnemonic(MNEMONIC)
    public_key = private_key.to_pubkey()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()
    obi = PyObi("{symbols:[string],multiplier:u64}/{rates:[u64]}")
    calldata = obi.encode(
    {"symbols": ["ETH", "BTC", "BAND", "MIR", "UNI"], "multiplier": 100})

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

    txn = (
        Trans()
        .with_messages(msg)
        .with_account_num(account_num)
        .with_sequence(sequence)
        .with_chain_id(CHAIN_ID)
        .with_gas(20000)
        .with_fee(100000)
        .with_memo('')
    )

    tx_raw_bytes = txn.get_tx_data(private_key, 20000000)
    t_send_tx_block_mode(c, tx_raw_bytes)
   


def t_get_data_source(c, id):
    print('------------- get_data_source----------------')
    # print(type(c.get_data_source(1)))
    print(c.get_data_source(id = 1))

def t_get_oracle_script(c, id):
    print('------------- get_oracle_script----------------')
    # print(type(c.get_oracle_script(1)))
    print(c.get_oracle_script(id = 1))

def t_get_request_by_id(c, id = 1):
    print('------------- get_request_by_id----------------')
    print(c.get_request_by_id(id))

def t_get_latest_block(c):
    print('------------- get_latest_block----------------')
    # print(type(c.get_latest_block()))
    print(c.get_latest_block())

def t_get_reporters(c, validator = "bandvaloper18tjynh8v0kvf9lmjenx02fgltxk0c6jmm2wcjc"): # Default validator for testing
    print('------------- get_reporters----------------')
    # print(type(c.get_reporters(validator)))
    print(c.get_reporters(validator))

def t_get_request_id_by_tx_hash(c, id = "AFC6BDDC7E7041B1AC21C26E25A52550689D148BE9A0D8E797E45DD753BF7FB3"):
    print('------------- get_request_id_by_tx_hash---------------')
    # print(type(c.get_request_id_by_tx_hash(HexBytes(id))))
    print(c.get_request_id_by_tx_hash(HexBytes(id)))

def t_get_account(c, addr = "band1ee656yzw6y9swqayu9v0kgu5pua2kgjq3hd6g3"):
    print('------------- get_account---------------')
    print(c.get_account(addr))

def t_send_tx_sync_mode(c, tx_byte):
    print(c.send_tx_sync_mode(tx_byte))

def t_send_tx_async_mode(c, tx_byte):
    print(c.send_tx_async_mode(tx_byte))

def t_send_tx_block_mode(c, tx_byte):
    print(c.send_tx_block_mode(tx_byte))

def t_get_latest_request(c):
    # Skip
    print('------------- get_latest_request----------------')
    latest_req_calldata = '000000003b9aca00'
    print(bytes(latest_req_calldata, 'utf-8'))
    # print(type(c.get_latest_request(37, bytes(latest_req_calldata, 'utf-8'), 10, 16)))
    print(c.get_latest_request(45, bytes(latest_req_calldata, 'utf-8'), 10, 16))

def t_get_price_symbol(c):
    # Skip 
    print('------------- get_price_symbol----------------')
    print(type(c.get_price_symbols(['BAND'], 10, 10)))
    print(c.get_price_symbols(['BAND'], 10, 10))

    

if __name__ == "__main__":
    main()
