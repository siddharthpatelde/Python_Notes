# PRINT FUNCTION – FULL USAGE GUIDE

# Basic Syntax:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Parameters:
# *objects → One or more objects to be printed (comma-separated).
# sep      → String inserted between objects. Default is ' ' (space).
# end      → String appended after the last object. Default is '\n' (new line).
# file     → A file-like object (stream); default is sys.stdout.
# flush    → If True, forcibly flush the stream. Default is False.

# --------------------------------------------

# 1. Basic print
print("Hello, World!")  # Hello, World!

# 2. Printing multiple objects
print("Hello", "Python", 3)  # Hello Python 3

# 3. Using 'sep' to change separator
print("2025", "05", "27", sep="-")  # 2025-05-27

# 4. Using 'end' to avoid new line
print("Loading", end="...")  # Loading...

# 5. Using custom separator and end together
print("Name", "Age", sep=": ", end=" years\n")  # Name: Age years

# 6. Printing to a file
with open("output.txt", "w") as f:
    print("Saving this line to a file.", file=f)

# 7. Forcing flush (useful in loops/real-time output)
import time
for i in range(3):
    print(i, end=" ", flush=True)
    time.sleep(0.5)  # Output appears immediately

# 8. Printing escape characters
print("Line1\nLine2")         # New line
print("Tabbed\tSpace")        # Tab space
print("He said \"hello\"")    # Quotes inside string

# 9. Printing with formatted strings (f-strings)
name = "Siddhart"
age = 21
print(f"Hello, my name is {name} and I am {age} years old.")

# 10. Using print with unpacking
nums = [1, 2, 3, 4]
print(*nums)                # 1 2 3 4
print(*nums, sep=", ")      # 1, 2, 3, 4

# 11. Printing Unicode/emojis (note: removed for LaTeX safety)
print("Python is fun")
