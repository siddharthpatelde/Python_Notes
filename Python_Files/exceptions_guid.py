# Lesson: Exceptions in Python

# 1. Handling runtime errors with try-except blocks

try:
    result = 5 / 0
except ZeroDivisionError:
    print("An error occurred: Division by zero")

# 2. Handling file errors specifically and generally

try:
    file = open("my_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file was not found")
except:
    print("An unspecified error has occurred")

# 3. Raising exceptions manually

x = -1
if x < 0:
    raise ValueError("The value must not be negative.")

# 4. Handling raised exceptions with custom messages

try:
    x = int(input("x = "))
    if x < 0:
        raise ValueError("The value must not be negative.")
except ValueError as exception:
    print(exception)

