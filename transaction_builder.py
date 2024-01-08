import json

from bitcoinlib.wallets import Wallet, wallet_delete_if_exists

NETWORK_MODE = "testnet"

"""sudo apt-get install python3.x-dev"""
ADDRESS_1 = "mhqFgt885yKTjwe8J5S9fvXNerDYKbFmi8"
PK_1 = "0fbeb4a8923e11afc9dec6fd17e887fb735ffcd154fd3adcad865fa23f47cabf"
AMOUNT_TO_TRANSFER = 100
ADDRESS_2 = "n4NpDkLY5NrXX1JYpLTriqVu6g8PRHcSjC"
PK_2 = "cQxQstpNBh4jknQcEEANRzpR6z2nYtNeLG38v1sm1PuuNCVSdRH8"

ADDRESS_3 = "mkfhR2Bap9axzu1QoeCX7DtPLcyGT6g7Fh"
PK_3 = "cTnEhjCaW1ezL7ynqEQ3KcFTv772RfZeefYcn4MHmtcicXGnFfmt"

WALLET_NAME_TEMPORARY = "First"
wallet_delete_if_exists(WALLET_NAME_TEMPORARY, force=True)
ADDRESS_FROM = ADDRESS_1
PK_FROM = PK_1

ADDRESS_TO = ADDRESS_2

w = Wallet.create(
    WALLET_NAME_TEMPORARY,
    keys=[PK_FROM],
    scheme='single',
    network=NETWORK_MODE
)
w.utxos_update(networks=[NETWORK_MODE])
w.transactions_update(network=NETWORK_MODE)
w.balance_update_from_serviceprovider(network=NETWORK_MODE)
w.scan(network=NETWORK_MODE)

# create raw transaction
TRANSACTION = w.send_to(
    to_address=ADDRESS_TO,
    amount=AMOUNT_TO_TRANSFER,
    network=NETWORK_MODE
)


def tx_builder(raw_tx):
    data_for_json = {
            "coin": "BTC",
            "amount": AMOUNT_TO_TRANSFER / 10**8,
            "address_from": ADDRESS_FROM,
            "address_to": ADDRESS_TO,
            "chain": "BTC",
            "raw_signed_tx": raw_tx
        }
    # next save it in file JSON
    with open('tx.json', 'w') as outfile:
        json.dump(data_for_json, outfile)

tx_builder(TRANSACTION.raw_hex())