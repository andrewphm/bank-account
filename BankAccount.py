import random


class BankAccount:
    balance = 0

    def __init__(
        self,
        full_name,
        account_type,
        account_number=random.randint(1000000, 99999999),
    ):
        self.full_name = full_name
        self.account_number = account_number
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += float(amount)
        print(f"Amount deposited: ${amount}. New Balance: ${self.balance:,.2f}")

    def withdraw(self, amount):
        self.balance -= float(amount)
        print(f"Amount withdrawn: ${amount}. New Balance: ${self.balance:,.2f}")

    def get_balance(self):
        print(f"Your current balance is: ${self.balance:,.2f}")
        return self.balance

    def add_interest(self):
        if self.account_type == "savings":
            interest_rate = 0.001
        else:
            interest_rate = 0.00083
        interest = self.balance * interest_rate
        self.balance += round(interest, 2)
        print(f"Monthly interest added. New balance: ${self.balance:,.2f}")

    def print_statement(self):
        account_number_str = str(self.account_number)

        print(
            f"{self.full_name}\nAccount No.: ****{account_number_str[4:]}\nBalance: ${self.balance:,.2f}"
        )


andrew_account = BankAccount("Andrew Pham", "chequing")
danny_account = BankAccount("Danny Phan", "savings")
jane_account = BankAccount("Jane Doe", "chequing")

andrew_account.deposit(100.24)
andrew_account.get_balance()
andrew_account.add_interest()


mitchell_account = BankAccount("Mitchell Doe", "savings", "03141592")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()
