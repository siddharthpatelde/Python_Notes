# FAMOUS DICTIONARY EXAMPLES USING: get(), keys(), values(), items()

student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science",
    "grade": "A"
}

# --------------------------------------------
# 1. .get() – Safe value access
# → Famous for avoiding KeyError if the key doesn't exist

# GOOD: get() returns default instead of crashing
print("Country:", student.get("country", "Not specified"))  # Not specified

# BAD: This would raise KeyError
# print(student["country"])

# --------------------------------------------
# 2. .keys() – Useful for looping or checking presence
print("Keys in student dict:")
for key in student.keys():
    print("-", key)

# Check if "age" is a key
if "age" in student.keys():
    print("Yes, 'age' is a key.")

# --------------------------------------------
# 3. .values() – Check or search values
print("Values in student dict:")
for value in student.values():
    print("-", value)

# Check if a specific value exists
if "Computer Science" in student.values():
    print("Found the major!")

# --------------------------------------------
# 4. .items() – Iterate over both key and value (most common in loops)
print("Student Info:")
for key, value in student.items():
    print(f"{key} → {value}")

# --------------------------------------------
# BONUS: Use in condition
if "grade" in student:
    if student["grade"] == "A":
        print("Excellent student!")

# --------------------------------------------
# 5. Finding Key from Value (reverse lookup)

# Let's say we want the key for value "A"
target_value = "A"

# Using a loop to search for matching value
for key, value in student.items():
    if value == target_value:
        print(f"Key for value '{target_value}' is: {key}")

# --------------------------------------------
# 6. Finding Value from Key (already known way)
# Just standard access
print("Grade is:", student["grade"])  # A
