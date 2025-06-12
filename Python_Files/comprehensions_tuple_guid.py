# TUPLE COMPREHENSIONS – PYTHON GUIDE

# → Tuple comprehensions work just like list comprehensions,
#   but use parentheses ( ) and the tuple() constructor.
#
# → Syntax:
#   tuple_result = tuple(expression for item in iterable if condition)

# Note:
# Although the syntax uses ( ), it does not create a tuple by default —
# you must explicitly wrap the comprehension in the tuple() constructor.


# --------------------------------------------
# 1. Tuple of squares (1 to 10)
squaretuples = tuple(x**2 for x in range(1, 11))
print("Tuple of Squares:", squaretuples)
# Output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# --------------------------------------------
# 2. Filter odd numbers from existing list of squares
squares = [x**2 for x in range(1, 11)]
odd_squaretuples = tuple(x for x in squares if x % 2 != 0)
print("Odd Squares as Tuple:", odd_squaretuples)
# Output: (1, 9, 25, 49, 81)

# --------------------------------------------
# 3. Filter words starting with 'b' from a tuple
words = ('apple', 'banana', 'cherry', 'durian', 'elderberry')
b_words = tuple(word for word in words if word.startswith('b'))
print("Words starting with 'b':", b_words)
# Output: ('banana',)
