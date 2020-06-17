from app import *

print("Welcome to Fintrack", "-"*20, sep="\n")

while True:
    print("\n", "-"*20, "\n")

    print("What would you like to do:\n\
        1. Create Wallet\n\
        2. Add Money to Wallet\n\
        3. Create Expense\n\
        4. Create Debt\n\
        5. Delete A Wallet\n\
        6. Delete Expense\n\
        7. Delete Debt\n\
        8. See All Transaction\n\
        9. Exit")

    exists = check_wallet()

    if not exists:
        print("Please create a new Wallet before you proceed!")

    choice = input("--> ")

    if choice == "1":
        create_wallet()

    elif choice == "2":
        topup_wallet()

    elif choice == "3":
        create_expense()

    elif choice == "5":
        delete_wallet()

    elif choice == "8":
        list_transactions()

    else:
        break
