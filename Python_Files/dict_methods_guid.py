# DICTIONARY METHODS – MOST IMPORTANT & COMMON

person = {
    "name": "Alice",
    "age": 22,
    "country": "Germany"
}

# --------------------------------------------
# 1. get(key[, default])
# → Returns the value for the key if it exists; otherwise returns default (or None)
print("get('name'):", person.get("name"))         # Alice
print("get('gender'):", person.get("gender"))     # None
print("get('gender', 'Not specified'):", person.get("gender", "Not specified"))

# --------------------------------------------
# 2. keys()
# → Returns a view of all keys
print("Keys:", person.keys())  # dict_keys(['name', 'age', 'country'])

# --------------------------------------------
# 3. values()
# → Returns a view of all values
print("Values:", person.values())  # dict_values(['Alice', 22, 'Germany'])

# --------------------------------------------
# 4. items()
# → Returns a view of all key-value pairs as tuples
print("Items:", person.items())  # dict_items([('name', 'Alice'), ('age', 22), ...])

# --------------------------------------------
# 5. pop(key)
# → Removes a key and returns its value
age = person.pop("age")
print("Popped 'age':", age)
print("After pop():", person)

# --------------------------------------------
# 6. popitem()
# → Removes and returns the last inserted (key, value) pair
last_item = person.popitem()
print("Popped last item:", last_item)
print("After popitem():", person)

# --------------------------------------------
# 7. update(other_dict)
# → Merges another dictionary into current one
person.update({"name": "Bob", "gender": "Male"})
print("After update():", person)

# --------------------------------------------
# 8. clear()
# → Removes all key-value pairs from dictionary
temp = {"x": 1, "y": 2}
temp.clear()
print("After clear():", temp)

# --------------------------------------------
# 9. copy()
# → Returns a shallow copy of the dictionary
original = {"a": 1, "b": 2}
duplicate = original.copy()
print("Copy:", duplicate)
