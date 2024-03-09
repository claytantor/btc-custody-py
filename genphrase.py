from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

# # Generate a 12-word mnemonic
# mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)

# print("Mnemonic:", mnemonic)

# seed = Bip39SeedGenerator(mnemonic).Generate()

# # Create a Bip44 object (for Bitcoin) and derive the account keys
# bip44_mst_ctx = Bip44.FromSeed(seed, Bip44Coins.BITCOIN)
# bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)

# # Derive the first address (index 0)
# bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)
# bip44_addr_ctx = bip44_chg_ctx.AddressIndex(0)

# print("Private Key:", bip44_addr_ctx.PrivateKey().ToWif())
# print("Public Key:", bip44_addr_ctx.PublicKey().RawCompressed().ToHex())
# print("Address:", bip44_addr_ctx.PublicKey().ToAddress())
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

# Generate a random private key
random_private_key = generate_random_private_key()

# Create a mnemonic from the private key
mnemonic_phrase = create_mnemonic_from_private_key(random_private_key)



print("Mnemonic Phrase:", mnemonic_phrase)
