from bitcoinlib.wallets import Wallet, wallet_delete_if_exists
from bitcoinlib.transactions import Transaction, Output
import shlex
import sys
import os

from bitcoinlib.keys import HDKey
from bitcoinlib.encoding import to_hexstring

from bitcoinlib.mnemonic import Mnemonic

def generate_random_private_key():
    # Generate 32 bytes (256 bits) of random data
    return os.urandom(32)

def create_mnemonic_from_private_key(private_key):
    # Create a mnemonic phrase from the provided private key
    mnemonic = Mnemonic().to_mnemonic(private_key)
    return mnemonic


if __name__ == '__main__':

    # the mnemonic phrase is passed as a command line argument
    wallet_name = sys.argv[1]
    
    # Generate a random private key
    random_private_key = generate_random_private_key()

    # Create a mnemonic from the private key
    mnemonic_phrase = create_mnemonic_from_private_key(random_private_key)

    wallet = Wallet.create(wallet_name, keys=mnemonic_phrase, network=os.getenv("BTC_NETWORK", "testnet"), witness_type='segwit')

    # Display some information about the wallet
    print("Wallet Info:")
    print("Mnemonic Phrase:", mnemonic_phrase)
    
    # convert the private key to a Wallet Import Format (WIF) string
    wif = to_hexstring(random_private_key)
    print("Private Key:", wif)


    print("ID:", wallet.wallet_id)
    print("Name:", wallet.name)
    print("Network:", wallet.network.name)
    print("Address:", wallet.get_key().address)