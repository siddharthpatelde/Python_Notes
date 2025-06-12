# DICTIONARIES – BASIC USAGE GUIDE

# 1. What is a dictionary?
# → A dictionary is a collection of key-value pairs.
# → Each key must be unique, and values can be of any type.

# Unlike lists or tuples (which store values), dictionaries store data like a "map":
#   Key   →   Value

# --------------------------------------------
# 2. Creating dictionaries

# Method 1: Using curly braces
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Method 2: Using dict() constructor
profile = dict(name="Bob", age=25)
print("Created with dict():", profile)

# --------------------------------------------
# 3. Accessing values

print("Name:", student["name"])  # Alice
print("Age:", student["age"])    # 21

# If key doesn't exist, it raises a KeyError
# print(student["grade"])  # KeyError

# --------------------------------------------
# 4. Adding new key-value pairs

student["grade"] = "A"
print("Updated student:", student)

# --------------------------------------------
# 5. Iterating over a dictionary (keys by default)

for key in student:
    print("Key:", key, "| Value:", student[key])
