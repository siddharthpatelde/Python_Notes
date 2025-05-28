# STRINGS – FULL USAGE GUIDE

# Basic Explanation:
# A string is a sequence of characters enclosed in single (' ') or double (" ") quotes.
# Strings are immutable in Python.

# --------------------------------------------
# 1. Creating Strings
name = 'math'     # single-quoted string
subject = "math"  # double-quoted string

# 2. String Addition and Printing
print("math" + "works")     # mathworks
print("math", "works")      # math works

# 3. String Multiplication
string1 = "hello"
string2 = "world"
number = 5

print(string1, string2)     # hello world
print(string1 + string2)    # helloworld
print(string1 * number)     # hellohellohellohellohello

# 4. Invalid Concatenation Example
# print(string1 + number)   # TypeError: can only concatenate str (not "int")

# STRING METHODS – TOP 10 DEFINITIONS

text = "hello WORLD"

# 5. capitalize()
# Returns string with first character uppercased, rest lowercased.
print(text.capitalize())  # Hello world

# 6. lower()
# Converts all characters to lowercase.
print(text.lower())       # hello world

# 7. title()
# Capitalizes first letter of each word.
print(text.title())       # Hello World

# 8. casefold()
# Aggressive lowercase, suitable for comparisons.
text2 = "Straße"
print(text2.casefold())   # strasse

# 9. upper()
# Converts all characters to uppercase.
print(text.upper())       # HELLO WORLD

# 10. count()
# Counts how many times a substring appears.
print(text.count("l"))            # 3
print(text.count("l", 3, 6))      # 1

# 11. find()
# Finds index of substring, or -1 if not found.
print(text.find("WORLD"))        # 6
print(text.find("not_here"))     # -1

# 12. replace()
# Replaces substring with another.
print(text.replace("WORLD", "Python"))     # hello Python
print(text.replace("l", "X", 2))           # heXXo WORLD

# 13. swapcase()
# Swaps uppercase to lowercase and vice versa.
print("Hello World".swapcase())  # hELLO wORLD

# 14. join()
# Joins elements of iterable with separator.
words = ["hello", "world"]
print("-".join(words))           # hello-world
