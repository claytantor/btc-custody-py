from bitcoinlib.wallets import Wallet, wallet_delete_if_exists, wallet_exists
from bitcoinlib.transactions import Transaction, Output
import sys
import os

from utils import get_db_url

if __name__ == '__main__':
    """
    This script lists all wallets in the wallet directory.
    """
    wallets = Wallet.list(db_uri=get_db_url())
    print("Wallets:")
    for wallet in wallets:
        print(wallet.name)
    print("Done")




