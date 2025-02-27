"""
Simple Scenario: Bank Account Management (Encapsulation)
In this scenario, we'll demonstrate encapsulation by creating a class BankAccount that encapsulates the details of a bank account, such as the account balance and methods to deposit or withdraw money. We will use getter and setter methods to access and modify the balance, ensuring that the balance can only be modified in controlled ways.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner # Account holder's name
        self.__balance = balance # Private variable to store account balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited amount : {amount} and account balance is : {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f"Withdrawn amount : {amount} and avilable balance is : {self.__balance}")
        else:
            print(f"Insufficiant balance. Balance is : {self.__balance}")

# create a object
account = BankAccount("Joshi")
account.deposit(2000)

account.withdraw(5000)

# Accessing the balance using the getter method
print(f"Final balance for {account.owner}: {account.get_balance()}")