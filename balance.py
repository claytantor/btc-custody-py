from bitcoinlib.wallets import Wallet, wallet_delete_if_exists, wallet_exists
from bitcoinlib.transactions import Transaction, Output
import sys
import os

if __name__ == '__main__':
    wallet_name = sys.argv[1]

    # Create a wallet for the sender
    if not wallet_exists(wallet_name): 
        print("Wallet does not exist")
        exit(1)

    wallet = Wallet(wallet_name)
    wallet.scan()
    wallet.info()

    wallet_balance = wallet.balance(network=os.getenv("BTC_NETWORK", "testnet"))
    print("Wallet Balance:", wallet_balance)



