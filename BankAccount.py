def returns_home():
    return "hello"


class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += float(amount)
        print(f"Amount deposited: ${amount}. New Balance: ${round(self.balance, 2)}")

    def withdraw(self, amount):
        self.balance -= float(amount)
        print(f"Amount withdrawn: ${amount}. New Balance: ${round(self.balance, 2)}")

    def get_balance(self):
        print(f"Your current balance is: ${self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += round(interest, 2)
        print(f"Monthly interest added. New balance: ${self.balance}")

    def print_statement(self):
        account_number_str = str(self.account_number)

        print(
            f"{self.full_name}\nAccount No.: ****{account_number_str[4:]}\nBalance: ${self.balance}"
        )


andrew_bank = BankAccount("Andrew Pham", 12345678, 100)
