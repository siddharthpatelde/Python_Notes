# KLASSEN UND OBJEKTE – PYTHON GUIDE

# → A class is a blueprint or template for creating objects.
# → An object is a concrete instance of a class with its own data and behavior.

# --------------------------------------------
# Example: A simple bank account class

class Account:
    # The constructor method (__init__) is called when an object is created
    def __init__(self, name, number):
        self.name = name          # Account holder
        self.number = number      # Account number
        self.balance = 0          # Initial balance is 0

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount    # Increase balance by the deposit amount

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount    # Decrease balance by the withdrawal amount

# --------------------------------------------
# Creating instances (objects) of the Account class

account1 = Account("Otto Schmidt", "123456789")
account2 = Account("Luisa Meier", "987654321")

# --------------------------------------------
# Using object methods
account1.deposit(100)
account1.withdraw(40)

account2.deposit(200)

# --------------------------------------------
# Accessing attributes
print("Account 1 - Name:", account1.name)
print("Account 1 - Balance:", account1.balance)

print("Account 2 - Name:", account2.name)
print("Account 2 - Balance:", account2.balance)
