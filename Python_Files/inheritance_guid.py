# INHERITANCE IN PYTHON (Vererbung)
# → Extending a base class (Account) with a derived class (SavingsAccount)

# Assuming Account class is already defined as in earlier chapters
class Account:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def getBalance(self):
        return self.__balance

    def __str__(self):
        return f"Name: {self.__name}, Kontonummer: {self.__number}, Guthaben: {self.__balance}"

# Subclass – Sparkonto mit Zinsen
class SavingsAccount(Account):
    def __init__(self, name, number, balance, interest):
        super().__init__(name, number)      # Call parent constructor
        self.deposit(balance)               # Set starting balance using inherited method
        self.__interest = interest          # Private interest rate for this account

    def add_interest(self):
        # Compute interest and deposit
        interest_amount = self.getBalance() * self.__interest
        self.deposit(interest_amount)

# -----------------------------------------
# Creating and using subclass objects

savings_account = SavingsAccount("Max Mustermann", "123456", 1000, 0.05)
print(savings_account.getBalance())    # Before interest: 1000

savings_account.add_interest()         # Add interest
print(savings_account.getBalance())    # After interest: 1050.0
