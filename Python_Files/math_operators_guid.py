# MATH OPERATORS – FULL USAGE GUIDE

# Basic Syntax:
# <operand1> <operator> <operand2>

# Operators:
# +   Addition            →  a + b
# -   Subtraction         →  a - b
# *   Multiplication      →  a * b
# /   Division            →  a / b
# //  Floor Division      →  a // b
# %   Modulus (Remainder) →  a % b
# **  Exponentiation      →  a ** b

# --------------------------------------------

# 1. Addition
print("1 + 1 =", 1 + 1)

# 2. Subtraction
print("2 - 3 =", 2 - 3)

# 3. Multiplication
print("4 * 5 =", 4 * 5)

# 4. Division (always returns float)
print("6 / 3 =", 6 / 3)

# 5. Floor Division (truncates decimals)
print("7 // 2 =", 7 // 2)

# 6. Rounded division result using round()
number1 = 1.85
number2 = 1.35
number3 = 1.5
print(f"{number1} rounded is:", round(number1))  # 2
print(f"{number2} rounded is:", round(number2))  # 1
print(f"{number3} rounded is:", round(number3))  # 2

# 7. Exponentiation
print("3 ** 3 =", 3 ** 3)  # 27

# 8. Modulus (Remainder)
print("20 / 6 =", 20 / 6)      # Division
print("20 % 6 =", 20 % 6)      # Remainder (2)

# 9. Operator Precedence in Python:
# 1. ()
# 2. **
# 3. * and /
# 4. + and -
# Evaluated left to right within same level
