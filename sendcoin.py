from bitcoinlib.wallets import Wallet, wallet_delete_if_exists, wallet_exists
from bitcoinlib.transactions import Transaction, Output
import sys
import os
from utils import calculate_fee_rate, get_db_url

if __name__ == '__main__':
    # Define sender and recipient information
    # sender_private_key = sys.argv[1]
    recipient_address = sys.argv[1]
    amount_to_send_btc:float = float(f'{sys.argv[2]}')  # Amount in BTC
    wallet_name = sys.argv[3]
    if len(sys.argv) > 4:
        speed = sys.argv[4]
    else:
        speed = "fastest"

    print("Recipient Address:", recipient_address)
    print("Amount to Send BTC:", amount_to_send_btc)

    amount_to_send_satoshi = int(amount_to_send_btc * 100000000)
    print("Amount to Send Satoshi:", amount_to_send_satoshi)

    # Create a wallet for the sender
    if not wallet_exists(wallet_name, db_uri=get_db_url()): 
        print("Wallet does not exist: {wallet_name}")
        exit(1)

    wallet = Wallet(wallet_name, db_uri=get_db_url())
    forward_fee=calculate_fee_rate(speed=speed)

    for key in wallet.keys(network=os.getenv("BTC_NETWORK", "testnet")):
        if key.balance:
            t = wallet.send_to(to_address=recipient_address,
                               network=os.getenv("BTC_NETWORK", "testnet"),
                               amount=int(key.balance-forward_fee),
                               fee=forward_fee, offline=False)
            if t:
                print(f"Transaction: {t}")




