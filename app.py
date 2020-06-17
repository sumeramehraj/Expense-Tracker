from model import *
from datetime import datetime

db.connect()

def create_wallet():
    name = input("Enter Name for the Wallet: ")
    wallet = Wallet(name=name, amount=0, last_transaction=datetime.now())
    wallet.save()
    print("Wallet Created Successfully..\nCurrent Balance: 0")


def check_wallet():
    wallets = Wallet.select()
    if len(wallets) == 0:
        return 0
    else:
        return 1


def list_wallets():
    wallets = Wallet.select()
    print("Select Wallet ID:")
    for wallet in wallets:
        print(wallet.id, wallet.name)

    wallet_id = int(input("-->"))
    return wallet_id


def topup_wallet():
    wallet_id = list_wallets()
    wallet = Wallet.get(Wallet.id == wallet_id)
    amount = int(input("Enter Amount to Add: "))
    wallet.amount += amount
    wallet.save()

    print(f"Current Balance : {wallet.amount}")


def create_expense():
    name = input("Enter Expense Name: ")
    amount = int(input("Enter Expense Amount: "))
    note = input("Add a Note\n---------------------------------------")
    wallet_id = list_wallets()
    wallet = Wallet.get(Wallet.id == wallet_id)
    expense = Expense(name=name, amount=amount, note=note,
                      wallet=wallet, timestamp=datetime.now())
    transaction = Transaction(amount=amount, wallet=wallet,
                              note=name, is_debit=True, timestamp=datetime.now())
    expense.save()
    transaction.save()


def delete_wallet():
    wallet_id = list_wallets()
    wallet = Wallet.get(Wallet.id == wallet_id)
    wallet.delete_instance()


def list_transactions():
    transactions = Transaction.select()
    for transaction in transactions:
        if transaction.is_debit:
            amount = "-₹" + str(transaction.amount)
        else:
            amount = "+₹" + str(transaction.amount)

        print(transaction.note, amount,
              transaction.wallet, transaction.timestamp, sep=" | ")
