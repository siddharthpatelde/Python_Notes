# OBJEKTVERWENDUNG – KONTOBEISPIEL

# → This example shows how to create and interact with objects
# → Using methods defined inside the Account class

# Assuming the class Account is already defined

# --------------------------------------------
# Creating objects from the class

account1 = Account("Otto Schmidt", "123456")
account2 = Account("Luisa Meier", "789012")

# --------------------------------------------
# Depositing money
account1.deposit(1500)
account2.deposit(500)
account2.deposit(800)

# --------------------------------------------
# Withdrawing money (if enough balance)
account1.withdraw(500)
print("Account 1 Balance:", account1.balance)  # Output: 1000

account2.withdraw(200)
print("Account 2 Balance:", account2.balance)  # Output: 1100

# --------------------------------------------
# Note:
# account1.balance refers to the attribute of a specific object
# Inside the class, we use self.balance since self refers to the current instance
