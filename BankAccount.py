from symbol import test_nocond


# test
class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount withdrawn: ${amount}. New Balance: ${self.balance}")

    def get_balance(self):
        print(f"Your current balance is: ${self.balance}")
        return self.balance
