"""A bank wants to manage customer accounts. Create a BankAccount class with a 
constructor to initialize account number and balance. Implement methods to deposit, 
withdraw, and display balance."""

class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Account {self.acc_no} balance: {self.balance}")

acc = BankAccount(1001, 5000)
acc.deposit(2000)
acc.withdraw(1500)
acc.withdraw(10000)
acc.show_balance()
