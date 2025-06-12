# LIST COMPREHENSIONS – PYTHON GUIDE

# → List comprehensions provide a concise way to create or transform lists.
# → Syntax: [ expression for item in iterable if condition ]
#
# Parts:
# expression → The output expression (what should be added to the new list)
# item       → The looping variable
# iterable   → Any iterable like range, list, tuple, etc.
# condition  → (Optional) Only items satisfying this condition are included


# --------------------------------------------
# 1. Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# --------------------------------------------
# 2. Filter odd squares from the above list
odd_squares = [x for x in squares if x % 2 != 0]
print("Odd Squares:", odd_squares)
# Output: [1, 9, 25, 49, 81]

# --------------------------------------------
# 3. Filter words starting with 'b'
words = ['apple', 'banana', 'cherry', 'durian', 'elderberry']
b_words = [word for word in words if word.startswith('b')]
print("Words starting with 'b':", b_words)
# Output: ['banana']

# --------------------------------------------
# 4. Example without condition (copying elements)
copied = [w for w in words]
print("Copied:", copied)

# --------------------------------------------
# 5. Example with inline modification
uppercased = [w.upper() for w in words]
print("Uppercased:", uppercased)
