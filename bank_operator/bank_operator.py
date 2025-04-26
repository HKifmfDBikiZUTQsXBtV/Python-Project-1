from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    (name, email) = (input("Enter name: "), input("Enter email: "))
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
    else:
        print('Email is valid')
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    print('list_users() works')
    if not len(users) == 0:
        for i in range(len(users)):
            print(f"{i+1}. {users[i]}")
    else:
        print('No users found')

def create_account():
    list_users()
    if len(users) != 0:
        idx = 0
        while True:
            try:
                idx = int(input("Select user number: ")) - 1
                user = users[idx]
                break
            except IndexError:
                print("Invalid user selection.\n")
                continue
            
        print("Account Type:")
        print("1. Savings Account")
        print("2. Students Account")
        print("3. Current Account")
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))

        if account_choice == 1:
            account = SavingsAccount(amount)
        elif account_choice == 2:
            account = StudentAccount(amount)
        elif account_choice == 3:
            account = CurrentAccount(amount)
        else:
            print("Invalid choice!")
            account = BankAccount(amount)

        users[idx].add_account(account)
        print(f"{account.get_account_type()} added!\n")
    else:
        print('No users currently available, so creating an account is not possible.')

def deposit_money():
    list_users()
    if len(users) != 0:
        while True:
            try:
                idx = int(input("Select user number: ")) - 1
                user = users[idx]
                break
            except IndexError:
                print("Invalid user selection.\n")
                continue
        
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
        while True:
            try:
                acc_idx = int(input("Select account: ")) - 1
                
                account = user.accounts[acc_idx]
                break
            except IndexError:
                print('Invalid account selection.\n')
                continue

        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    else:
        print('This operation cannot be processed, as the number of users are 0')

def withdraw_money():
    list_users()
    if len(users) != 0:
        while True:
            try:
                idx = int(input("Select user number: ")) - 1
                user = users[idx]
                break
            except IndexError:
                print("Invalid user selection.\n")
                continue
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
        while True:
            try:
                acc_idx = int(input("Select account: ")) - 1
                
                account = user.accounts[acc_idx]
                break
            except IndexError:
                print('Invalid account selection.\n')
                continue
        amount = float(input("Enter amount to withdraw: "))
        try:
            account.withdraw(amount)
            print("Withdrawal successful.\n")
        except ValueError as e:
            print(f"Error: {e}\n")
    else:
        print('This operation cannot be processed, as the number of users are 0')

def view_transactions():
    list_users()
    if len(users) != 0:
        while True:
            try:
                idx = int(input("Select user number: ")) - 1
                user = users[idx]
                break
            except IndexError:
                print("Invalid user selection.\n")
                continue
        for i, acc in enumerate(user.accounts):
            print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
            for tx in acc.get_transaction_history():
                print(tx)
    else:
        print('This operation cannot be processed, as the number of users are 0')