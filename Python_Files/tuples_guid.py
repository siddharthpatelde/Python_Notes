# TUPLES – FULL USAGE GUIDE

# 1. What is a tuple?
# → A tuple is an immutable, ordered collection of items.
# → Defined using parentheses: ()

# 2. Tuple vs List – Key Differences:
# → Tuples use ()     → Lists use []
# → Tuples are immutable → Lists are mutable (can be changed)
# → Tuples have fewer built-in methods
# → Tuples are faster and used for fixed data

# --------------------------------------------
# 3. Defining tuples

empty_tuple = ()
single_item = ("apple",)   # Note the comma!
fruits = ("apple", "banana", "cherry")

print("Fruits tuple:", fruits)
print("First item:", fruits[0])

# --------------------------------------------
# 4. What can we do with tuples?

# Tuple concatenation
more_fruits = ("mango", "orange")
combined = fruits + more_fruits
print("Combined tuple:", combined)

# Tuple unpacking
x, y, z = fruits
print("Unpacked:", x, y, z)

# Cannot change a tuple element
# fruits[0] = "kiwi"  # TypeError

# Cannot append or remove items
# fruits.append("kiwi")  # AttributeError
# fruits.remove("banana")  # AttributeError

# You can delete the whole tuple
temp = (1, 2, 3)
del temp
# print(temp)  # NameError if uncommented

# --------------------------------------------
# 5. Built-in functions usable with tuples

values = (10, 20, 5, 30)

# 1. len()
print("Length:", len(values))  # 4

# 2. max()
print("Maximum:", max(values))  # 30

# 3. min()
print("Minimum:", min(values))  # 5

# 4. tuple() constructor
sample_list = ["x", "y", "z"]
converted = tuple(sample_list)
print("Converted to tuple:", converted)
