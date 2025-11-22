#build a BankAccount class with deposit, withdraw, and balance methods.

class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return f"Current balance: ${self.balance:.2f}"
    
# Example usage
account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.get_balance())
account.withdraw(80)
print(account.get_balance())
account.deposit(-20)
print(account.get_balance())


