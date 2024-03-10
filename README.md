# CLI scripts for bitcoin
Self custody for bitcoin doesn't require a hardware wallet, really you can do anything that a hardware wallet gives you with  some basic pythonic skills and a laptop.

NOTE: The bincoinlib library uses a local wallet database to relate the wallet name to the key that it stores locally. It is stored at ~/.bitcoinlib and can be deleted. It is also possible to encrypt it. To do so refer to https://bitcoinlib.readthedocs.io/en/latest/source/_static/manuals.sqlcipher.html

## delete the wallet database
`rm -rvf ~/.bitcoinlib`

## create wallet
Generate a new wallet and store the mnemonic in a safe place.
`BTC_NETWORK=bitcoin python createwallet.py py_wallet_1`

## balance
Check the balance of a wallet
`BTC_NETWORK=bitcoin python balance.py py_wallet_1`

## restore wallet
Restore a wallet from a mnemonic
`BTC_NETWORK=bitcoin python restorewallet.py py_wallet_2 exhaust analyst liar seat access flat tunnel december army speed foam route wrist guess behind vacant output orient bless cradle garment corn limb plug`

## sendcoin
Send some coin to an address
`BTC_NETWORK=bitcoin python sendcoin.py bc1qd7w9zsrmgf8sgqpunntdyaca99yk5hqd3vdrwx 0.0001 py_wallet_2`

## trezor12
Create a 12 word mnemonic
`BTC_NETWORK=bitcoin python trezor12.py`

