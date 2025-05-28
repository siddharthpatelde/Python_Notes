# IF / ELSE / ELIF – FULL USAGE GUIDE

# Basic Syntax:
# if condition:
#     block of code
# elif another_condition:
#     another block
# else:
#     fallback block

# Conditional Operators:
# ==   → Equal to                  → (x == y)
# !=   → Not equal to              → (x != y)
# <    → Less than                 → (x < y)
# <=   → Less than or equal to     → (x <= y)
# >    → Greater than              → (x > y)
# >=   → Greater than or equal to  → (x >= y)

# Logical Operators:
# and  → True if both are True     → (x > 5 and x < 10)
# or   → True if at least one is True → (x > 5 or x < 3)
# not  → Inverts the truth value   → not (x > 5)

# --------------------------------------------

# 1. Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# 3. if-elif-else ladder
grade = 85
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 4. Nested if statements
number = 42
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number or zero")

# 5. Using logical 'and'
age = 25
if age > 18 and age < 65:
    print("Adult and working age")

# 6. Using logical 'or'
language = "Python"
if language == "Python" or language == "Java":
    print("Popular programming language")

# 7. Using logical 'not'
is_logged_in = False
if not is_logged_in:
    print("User not logged in")

# 8. Short form if-else (Ternary Expression)
# ➤ Python provides a one-line shorthand for simple if-else statements.
# → Syntax: value_if_true if condition else value_if_false
# → Returns: One of two values based on the boolean result of the condition.

value = 8

# Traditional if-else version:
if value % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print("Traditional form:", result)  # Even

# Shortened using ternary expression:
result = "Even" if value % 2 == 0 else "Odd"
print("Ternary form:", result)      # Even

