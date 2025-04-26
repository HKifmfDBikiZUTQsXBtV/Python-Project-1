class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self): 
        total_balance = 0
        for i in self.accounts:
            total_balance += i.balance
        return total_balance

    def get_account_count(self):
        account_count = len(self.accounts)
        return account_count

    def remove_account(self, account):
        return "Account"

    def is_valid_email(self,email):
        if '@gmail.com' in email:
            return True
        else:
            print("Invalid email address!")

    def __str__(self):
        return f"""
Name: {self.name} 
Email: {self.email} 
Number of Accounts: {self.get_account_count()} account(s)
Total Balance: ${self.get_total_balance()}
"""
