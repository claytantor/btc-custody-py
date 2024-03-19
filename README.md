# CLI scripts for bitcoin
Self custody for bitcoin doesn't require a hardware wallet, really you can do anything that a hardware wallet gives you with  some basic pythonic skills and a laptop.

NOTE: The bincoinlib library uses a local wallet database to relate the wallet name to the key that it stores locally. This implementation requires you to specify a password for db encryption, when that is given using the ENV_VAR `DB_PASSWORD` a database file called `bcl_encrypted.db` is saved in the progeam directory. It is also possible to configure other encryption. To do so refer to https://bitcoinlib.readthedocs.io/en/latest/source/_static/manuals.sqlcipher.html

## delete the wallet database
`rm -rvf ~/.bitcoinlib`

## create wallet
Generate a new wallet and store the mnemonic in a safe place.
`BTC_NETWORK=bitcoin python createwallet.py py_wallet_1 12`

## balance
Check the balance of a wallet
`BTC_NETWORK=bitcoin python balance.py py_wallet_2`

## restore wallet
Restore a wallet from a mnemonic
`BTC_NETWORK=bitcoin python restorewallet.py py_wallet_2 exhaust analyst liar seat access flat tunnel december army speed foam route wrist guess behind vacant output orient bless cradle garment corn limb plug`

## sendcoin
Send some coin to an address
`BTC_NETWORK=bitcoin python sendcoin.py bc1qd7w9zsrmgf8sgqpunntdyaca99yk5hqd3vdrwx 0.0001 py_wallet_2 fast`

## get wallet address
`BTC_NETWORK=bitcoin python getaddr.py py_wallet_2`

# encrypt the database
-rw-r--r-- 1 clay clay 139264 Mar 10 01:01 bcl.db
`DB_PASSWORD=soopersecret python encryptdb.py`

# decrypt the database
`DB_PASSWORD=soopersecret python decryptdb.py`

## list wallets
```bash
clw --database bcl.db
Command Line Wallet - BitcoinLib 0.6.14

BitcoinLib wallets:
[1] py_wallet_2 (bitcoin) 
[2] py_wallet_3 (bitcoin) 
```

