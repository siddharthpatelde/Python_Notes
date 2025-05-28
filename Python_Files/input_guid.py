# INPUT FUNCTION – FULL USAGE GUIDE

# Basic Syntax:
# input(prompt='')

# Parameters:
# prompt → A string, written to standard output without a trailing newline,
#           to ask the user for input. Default is an empty string ''.
# Returns → A string entered by the user (always str type).
# Notes   → Always returns a string. You need to convert it using int(), float(), etc. if needed.

# --------------------------------------------

# 1. Basic usage with no prompt
user_input = input()
print("You entered:", user_input)

# 2. Input with a prompt
name = input("Enter your name: ")
print("Hello,", name)

# 3. Converting input to integer
age = int(input("Enter your age: "))
print("You will be", age + 1, "next year.")

# 4. Converting input to float
height = float(input("Enter your height in meters: "))
print("Your height in cm is", height * 100)

# 5. Reading multiple values (as strings)
x, y = input("Enter two words separated by space: ").split()
print("Word 1:", x)
print("Word 2:", y)

# 6. Reading and converting multiple values to int
a, b = map(int, input("Enter two integers: ").split())
print("Sum =", a + b)

# 7. Reading many values into a list of ints
numbers = list(map(int, input("Enter multiple numbers: ").split()))
print("You entered:", numbers)

# 8. Handling invalid input using try/except
try:
    salary = float(input("Enter your monthly salary: "))
    print("Yearly salary:", salary * 12)
except ValueError:
    print("Invalid input! Please enter a number.")


