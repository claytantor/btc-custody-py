from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum, Bip39SeedGenerator
from bitcoinlib.wallets import Wallet, wallet_delete_if_exists, wallet_exists
from bitcoinlib.keys import HDKey
import sys
import os

from bitcoinlib.keys import HDKey
from bitcoinlib.encoding import to_hexstring
from bitcoinlib.mnemonic import Mnemonic

from utils import get_db_url

def generate_random_private_key():
    # Generate 32 bytes (256 bits) of random data
    return os.urandom(32)

def create_mnemonic_from_private_key(private_key):
    # Create a mnemonic phrase from the provided private key
    mnemonic = Mnemonic().to_mnemonic(private_key)
    return mnemonic

def create_mnemonic(word_count:int):
    # Create a mnemonic phrase from the provided private key
    if word_count != 12 and word_count != 24:
        print("Word count must be 12 or 24")
        sys.exit(1)

    if word_count == 12:
        # Generate a 12-word mnemonic
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
    else:
        # Generate a 24-word mnemonic
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)

    print("Mnemonic:", mnemonic)
    return mnemonic



if __name__ == '__main__':

    


    # the mnemonic phrase is passed as a command line argument
    wallet_name = sys.argv[1]

    # Create a wallet for the sender
    if  wallet_exists(wallet_name, db_uri=get_db_url()): 
        print("Wallet exists")
        exit(1)

     # the number of words in the mnemonic phrase
    word_count = sys.argv[2]
    word_count = int(word_count)
    
    # Create a mnemonic from the private key
    mnemonic_phrase = create_mnemonic(word_count)
    # Wallet.create('bcltestwlt4', network='bitcoinlib_test', db_uri=db_uri)
    wallet = Wallet.create(wallet_name, keys=mnemonic_phrase.ToStr(), network=os.getenv("BTC_NETWORK", "testnet"), witness_type='segwit', db_uri=get_db_url())

    # print the private key from the mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic_phrase).Generate()
    master_key = HDKey.from_seed(seed_bytes, network="bitcoin")

    # Display some information about the wallet
    print("Wallet Info:")
    print("Mnemonic Phrase:", mnemonic_phrase)
    print("Private key:", master_key)
    print("ID:", wallet.wallet_id)
    print("Name:", wallet.name)
    print("Network:", wallet.network.name)
    print("Address:", wallet.get_key().address)