from bitcoinlib.wallets import Wallet, wallet_delete_if_exists
from bitcoinlib.transactions import Transaction, Output
import shlex
import sys
import os
from bitcoinlib.keys import HDKey
from bitcoinlib.encoding import to_hexstring
from bitcoinlib.mnemonic import Mnemonic

if __name__ == '__main__':

    # the mnemonic phrase is passed as a command line argument
    wallet_name = sys.argv[1]
    mnemonic_phrase = " ".join(sys.argv[2:26])
    
    wallet = Wallet.create(wallet_name, keys=mnemonic_phrase, network=os.getenv("BTC_NETWORK", "testnet"), witness_type='segwit')

    # Display some information about the wallet
    print("Wallet Info:")
    print("Mnemonic Phrase:", mnemonic_phrase)
    print("ID:", wallet.wallet_id)
    print("Name:", wallet.name)
    print("Network:", wallet.network.name)
    print("Address:", wallet.get_key().address)