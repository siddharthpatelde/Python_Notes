# LIST METHODS – GENERAL PURPOSE

# Lists are mutable and support many built-in methods for adding, removing, searching, and modifying.

# 1. append()
# → Adds a single element to the end
items = ["pen", "book"]
items.append("pencil")
print("append():", items)

# 2. insert()
# → Inserts an element at a specific index
items.insert(1, "eraser")
print("insert():", items)

# 3. remove()
# → Removes the first matching value
items.remove("book")
print("remove():", items)

# 4. pop()
# → Removes and returns element at index (default = last)
removed = items.pop()
print("pop():", removed)
print("After pop:", items)

# 5. clear()
# → Empties the list
temp = ["a", "b"]
temp.clear()
print("clear():", temp)

# 6. copy()
# → Returns a shallow copy
original = ["x", "y", "z"]
cloned = original.copy()
print("copy():", cloned)

# 7. extend()
# → Adds multiple elements from another iterable
tools = ["pen", "pencil"]
tools.extend(["marker", "sharpener"])
print("extend():", tools)

# 8. index()  [Use with care]
# → Finds index of first match; raises error if not found
names = ["Alice", "Bob", "Charlie"]
try:
    idx = names.index("Bob")
    print("index():", idx)
except ValueError:
    print("Name not found")

# Alternative using 'in'
print("Eve" in names)  # False

# 9. count()
# → Counts number of times an item appears
letters = ["a", "b", "a", "c", "a"]
print("count():", letters.count("a"))  # 3

# 10. reverse()
# → Reverses the list in-place
words = ["start", "middle", "end"]
words.reverse()
print("reverse():", words)

# 11. sort() [Only works if items are comparable]
# → Sorts the list (only if all items can be compared)
languages = ["python", "c", "java"]
languages.sort()
print("sort():", languages)
