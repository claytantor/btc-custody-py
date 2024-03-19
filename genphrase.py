from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from bitcoinlib.wallets import Wallet, wallet_delete_if_exists
from bitcoinlib.transactions import Transaction, Output
import sys

from bitcoinlib.keys import HDKey
from bitcoinlib.encoding import to_hexstring

from bitcoinlib.mnemonic import Mnemonic


if __name__ == '__main__':

    # the mnemonic phrase is passed as a command line argument
    wallet_name = sys.argv[1]

    # the number of words in the mnemonic phrase
    word_count = sys.argv[2]

    word_count = int(word_count)
    # wordcount must be 12 or 24 
    if word_count != 12 and word_count != 24:
        print("Word count must be 12 or 24")
        sys.exit(1)

    if word_count == 12:
        # Generate a 12-word mnemonic
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
    else:
        # Generate a 24-word mnemonic
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)

    # print the private key from the mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    master_key = HDKey.from_seed(seed_bytes, network="bitcoin")

    print("Mnemonic:", mnemonic)
    print("Master key:", master_key)