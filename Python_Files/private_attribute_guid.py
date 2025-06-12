# PRIVATE ATTRIBUTES – GETTERS & __str__ EXAMPLE

# → A class with private attributes
# → Demonstrates data protection using __ (double underscore)
# → Includes a getter method and __str__() for safe access

class Account:
    def __init__(self, name, number):
        self.__name = name           # private attribute
        self.__number = number       # private attribute
        self.__balance = 0           # private attribute initialized to 0

    def deposit(self, amount):
        self.__balance += amount     # internally modifying balance is allowed

    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def getBalance(self):
        return self.__balance        # getter for balance

    def __str__(self):
        return f"Name: {self.__name} Kontonummer: {self.__number} Guthaben: {self.__balance}"

# --------------------------------------------
# Object creation and access
account3 = Account("Simon Frank", 6543211)
account3.deposit(1000)

# Attempting direct access (NOT RECOMMENDED)
# account3.__balance -= 1000000  Illegal access (will not modify balance)

# Safe balance access
print(account3.getBalance())  #1000

# Print uses __str__ internally
print(account3)  # Name: Simon Frank Kontonummer: 6543211 Guthaben: 1000
