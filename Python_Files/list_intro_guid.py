# LISTS – INTRODUCTION

# What is a list?
# A list is a built-in data structure in Python that stores an ordered collection of items.
# Lists are mutable, meaning you can change their contents after creation.
# Defined using square brackets: []

# --------------------------------------------
# 1. Defining a simple list (homogeneous)
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# 2. List of numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)

# 3. List of mixed data types
mixed = ["hello", 42, 3.14, True]
print("Mixed list:", mixed)

# 4. Empty list
empty = []
print("Empty list:", empty)

# 5. Nested list (list inside a list)
matrix = [[1, 2], [3, 4]]
print("Nested list:", matrix)

# 6. List using list() constructor
from_string = list("hello")
print("List from string:", from_string)  # ['h', 'e', 'l', 'l', 'o']

# 7. List from range()
range_list = list(range(5))
print("List from range():", range_list)  # [0, 1, 2, 3, 4]
