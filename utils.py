import sys
import os

# use from Crypto.Cipher import AES to encrypt the file
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2, scrypt
import os
import hashlib
import hmac
import random

def get_db_url():

    # get the path of the file
    # Get the path of the main Python file
    main_file_path = os.path.abspath(__file__)  # Absolute path of the main Python file

    # Define the relative path of the file you want
    relative_file_path = "bcl.db"

    # Combine the paths to get the absolute path of the file
    absolute_file_path = os.path.join(os.path.dirname(main_file_path), relative_file_path)

    db_uri = f'sqlite:///{absolute_file_path}'

    return db_uri

def derive_key_from_password(password, salt, key_length):
    # Use PBKDF2 with HMAC-SHA256 to derive a key from the password and salt
    key = PBKDF2(password, salt, dkLen=key_length, count=1000000, prf=lambda p, s: hmac.new(p, s, hashlib.sha256).digest())
    return key

def encrypt_db():
    password = os.getenv("DB_PASSWORD", "")
    if password == "":
        print("DB_PASSWORD environment variable not set")
        sys.exit(1)

    # get the path of the file
    # Get the path of the main Python file
    main_file_path = os.path.abspath(__file__)  # Absolute path of the main Python file

    # Define the relative path of the file you want
    relative_file_path = "bcl.db"

    # Combine the paths to get the absolute path of the file
    absolute_file_path = os.path.join(os.path.dirname(main_file_path), relative_file_path)

    encrypt_binary_file(absolute_file_path, absolute_file_path + ".enc", password)

def decrypt_db():
    password = os.getenv("DB_PASSWORD", "")
    if password == "":
        print("DB_PASSWORD environment variable not set")
        sys.exit(1)

    # get the path of the file
    # Get the path of the main Python file
    main_file_path = os.path.abspath(__file__)  # Absolute path of the main Python file

    # Define the relative path of the file you want
    relative_file_path = "bcl.db"

    # Combine the paths to get the absolute path of the file
    absolute_file_path = os.path.join(os.path.dirname(main_file_path), relative_file_path)

    decrypt_binary_file(absolute_file_path + ".enc", absolute_file_path, password)


def encrypt_file(input_file, output_file, password):

    # Generate a random 16-byte salt
    salt = get_random_bytes(16)

    # Derive a 256-bit (32 bytes) key from the password and salt
    key = derive_key_from_password(password, salt, 32)

    # Initialize AES cipher in ECB mode with the provided key
    cipher = AES.new(key, AES.MODE_ECB)

    # Read the contents of the input file
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Pad the plaintext to be a multiple of 16 bytes (AES block size)
    padded_plaintext = plaintext + b"\0" * (AES.block_size - len(plaintext) % AES.block_size)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Write the ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

def decrypt_file(input_file, output_file, password):
    # Read the salt and ciphertext from the input file
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        ciphertext = f.read()

    # Derive the key from the password and salt
    key = derive_key_from_password(password, salt, 32)

    # Initialize AES cipher in ECB mode with the derived key
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Write the plaintext to the output file
    with open(output_file, 'wb') as f:
        f.write(plaintext.rstrip(b"\0"))  # Remove padding

def encrypt_binary_file(input_file, output_file, password):
    # Generate a random 16-byte salt
    salt = get_random_bytes(16)

    # Derive a 256-bit (32 bytes) key from the password and salt
    key = derive_key_from_password(password, salt, 32)

    # Initialize AES cipher in CBC mode with the derived key and a random IV
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the binary data from the input file
    with open(input_file, 'rb') as f:
        binary_data = f.read()

    # Encrypt the binary data
    ciphertext = cipher.encrypt(binary_data)

    # Write the salt, IV, and ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(salt + iv + ciphertext)

def decrypt_binary_file(input_file, output_file, password):
    # Read the salt, IV, and ciphertext from the input file
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        iv = f.read(AES.block_size)
        ciphertext = f.read()

    # Derive the key from the password and salt
    key = derive_key_from_password(password, salt, 32)

    # Initialize AES cipher in CBC mode with the derived key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Write the decrypted binary data to the output file
    with open(output_file, 'wb') as f:
        f.write(plaintext)

def overwrite_file_with_random_data(file_path):
    # Open the file in write mode
    with open(file_path, 'wb') as f:
        # Get the size of the file
        file_size = os.path.getsize(file_path)
        
        # Generate random bytes equal to the size of the file
        random_data = bytearray(random.getrandbits(8) for _ in range(file_size))
        
        # Write the random data to the file
        f.write(random_data)