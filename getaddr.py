from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum, Bip39SeedGenerator
from bitcoinlib.wallets import Wallet, wallet_delete_if_exists, wallet_exists
from bitcoinlib.keys import HDKey
import sys
import os

from bitcoinlib.keys import HDKey
from bitcoinlib.encoding import to_hexstring
from bitcoinlib.mnemonic import Mnemonic

from utils import get_db_url

if __name__ == '__main__':

    # the mnemonic phrase is passed as a command line argument
    wallet_name = sys.argv[1]
    
    if not wallet_exists(wallet_name, db_uri=get_db_url()): 
        print("Wallet does not exist")
        exit(1)

    wallet = Wallet(wallet_name, db_uri=get_db_url())

    # get wallet info
    print("Wallet Info:")
    print("ID:", wallet.wallet_id)
    print("Name:", wallet.name)
    print("Network:", wallet.network.name)
    print("Address:", wallet.get_key().address)
