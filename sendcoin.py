from bitcoinlib.wallets import Wallet, wallet_delete_if_exists, wallet_exists
from bitcoinlib.transactions import Transaction, Output
import sys
import os

if __name__ == '__main__':
    # Define sender and recipient information
    # sender_private_key = sys.argv[1]
    recipient_address = sys.argv[1]
    amount_to_send_btc:float = float(f'{sys.argv[2]}')  # Amount in BTC
    wallet_name = sys.argv[3]

    print("Recipient Address:", recipient_address)
    print("Amount to Send BTC:", amount_to_send_btc)

    amount_to_send_satoshi = int(amount_to_send_btc * 100000000)
    print("Amount to Send Satoshi:", amount_to_send_satoshi)

    # Create a wallet for the sender
    if not wallet_exists(wallet_name): 
        print("Wallet does not exist")
        exit(1)

    wallet = Wallet(wallet_name)
    wallet.scan()
    wallet.info()

    wallet_balance = wallet.balance(network=os.getenv("BTC_NETWORK", "testnet"))
    print("Wallet Balance:", wallet_balance)

    if(amount_to_send_satoshi > wallet_balance):
        print("Insufficient funds")
        exit(1)
    
    txid = wallet.send_to(recipient_address, amount_to_send_satoshi, offline=False)
    print(f"Transaction ID: {txid}")


