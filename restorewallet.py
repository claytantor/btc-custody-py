from bitcoinlib.wallets import Wallet, wallet_exists
from bip_utils import Bip39SeedGenerator
import shlex
import sys
import os
from bitcoinlib.keys import HDKey
from bitcoinlib.encoding import to_hexstring
from bitcoinlib.mnemonic import Mnemonic
from utils import get_db_url

if __name__ == '__main__':

    # the mnemonic phrase is passed as a command line argument
    wallet_name = sys.argv[1]

    # Create a wallet for the sender
    if  wallet_exists(wallet_name, db_uri=get_db_url()): 
        print("Wallet exists")
        exit(1)

    if len(sys.argv) == 26:
        mnemonic_phrase = " ".join(sys.argv[2:26])
    elif len(sys.argv) == 14:
        mnemonic_phrase = " ".join(sys.argv[2:14])
    else:
        print("Invalid number of arguments")
        sys.exit(1)
    
    wallet = Wallet.create(wallet_name, keys=mnemonic_phrase, network=os.getenv("BTC_NETWORK", "testnet"), witness_type='segwit', db_uri=get_db_url())

    # print the private key from the mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic_phrase).Generate()
    master_key = HDKey.from_seed(seed_bytes, network="bitcoin")

    # Display some information about the wallet
    print("Wallet Info:")
    print("Mnemonic Phrase:", mnemonic_phrase)
    print("Private Key:", master_key)
    print("ID:", wallet.wallet_id)
    print("Name:", wallet.name)
    print("Network:", wallet.network.name)
    print("Address:", wallet.get_key().address)