# SETS – GENERAL USAGE GUIDE

# 1. What is a set?
# → A set is an unordered, unindexed collection with no duplicate elements.
# → Defined using curly braces {} or the set() constructor.

# --------------------------------------------
# 2. Creating a set

# From a list with duplicates
values = [2, 3, 3, 4, 5]
unique_values = set(values)
print("Set from list:", unique_values)  # {2, 3, 4, 5}

# Direct set definition
colors = {"red", "green", "blue"}
print("Set of colors:", colors)

# Empty set must be created using set()
empty_set = set()
print("Empty set:", empty_set)

# --------------------------------------------
# 3. General set methods

# 1. add()
colors.add("yellow")
print("After add():", colors)

# 2. remove()
colors.remove("green")  # Raises error if not found
print("After remove():", colors)

# 3. discard()
colors.discard("blue")  # Safe: no error if not found
print("After discard():", colors)

# 4. pop()
item = colors.pop()  # Removes random item (sets are unordered)
print("Popped:", item)

# 5. clear()
numbers = {1, 2, 3}
numbers.clear()
print("After clear():", numbers)

# 6. copy()
original = {"a", "b"}
cloned = original.copy()
print("Copy of set:", cloned)

# 7. update()
colors.update({"white", "black"})
print("After update():", colors)

# --------------------------------------------
# Sets do NOT support indexing or duplicate elements.
