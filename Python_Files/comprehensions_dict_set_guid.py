# DICTIONARY & SET COMPREHENSIONS – PYTHON GUIDE

# → Comprehensions allow building new dictionaries and sets in a single line.
# → They use similar syntax to list comprehensions with minor differences.

# --------------------------------------------
# DICTIONARY COMPREHENSION
# Syntax:
# {key_expression: value_expression for item in iterable if condition}

# Example: Square values in a dictionary only if value is even
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

squares = {key: value**2 for key, value in numbers.items() if value % 2 == 0}
print("Squared Even Values:", squares)
# Output: {'b': 4, 'd': 16}

# --------------------------------------------
# SET COMPREHENSION
# Syntax:
# {expression for item in iterable if condition}

# Example: Squaring all values in a set
nums = {-2, -1, 0, 1, 2}
squared_set = {num**2 for num in nums}
print("Squared Set:", squared_set)
# Output: {0, 1, 4}
