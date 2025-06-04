# FOR LOOP – FULL USAGE GUIDE

# Basic Syntax:
# for variable in iterable:
#     block of code

# --------------------------------------------
# 1. Using range()
# range(stop) → from 0 to stop-1
# range(start, stop) → from start to stop-1
# range(start, stop, step)

for i in range(5):
    print("i =", i)

for i in range(2, 6):
    print("From 2 to 5:", i)

for i in range(10, 0, -2):
    print("Countdown by 2:", i)

# --------------------------------------------
# 2. Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# 3. Iterating over a string
text = "hello"
for char in text:
    print("Char:", char)

# 4. Iterating over a tuple
# A tuple is an ordered, immutable collection.
# You can iterate through it just like a list.
coordinates = (10, 20, 30)
for value in coordinates:
    print("Value:", value)


# 5. Iterating over a set
# A set is an unordered collection of unique elements.
# Iteration works, but order is not guaranteed.
unique_numbers = {1, 2, 3}
for num in unique_numbers:
    print("Unique:", num)


# 6. Iterating over a dictionary
# A dictionary stores key-value pairs.
# Iterating over it by default gives you the keys.
person = {"name": "Alice", "age": 25}
for key in person:
    print("Key:", key, "| Value:", person[key])

# 7. Iterating with .items()
# .items() returns a list of (key, value) pairs from a dictionary.
# Useful when you need both key and value at once.
for key, value in person.items():
    print(f"{key} => {value}")

# 8. Using enumerate()
# enumerate() gives both the index and the item during iteration.
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")


# 9. Using break
for n in range(5):
    if n == 3:
        break
    print("Breaking loop at:", n)

# 10. Using continue
for n in range(5):
    if n == 2:
        continue
    print("Continuing:", n)

# 11. Using else with for
for n in range(3):
    print(n)
else:
    print("Loop completed without break.")

# --------------------------------------------
# range() – Recap:
# range(stop)
# range(start, stop)
# range(start, stop, step)
# returns a range object which is an iterable of numbers
