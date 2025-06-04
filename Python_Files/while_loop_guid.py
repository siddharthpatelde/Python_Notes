# WHILE LOOP – FULL USAGE GUIDE

# Basic Syntax:
# while condition:
#     block of code

# The code inside the loop runs repeatedly as long as the condition is True.

# --------------------------------------------

# 1. Basic while loop
counter = 0
while counter < 5:
    print("Counter is:", counter)
    counter += 1  # same as: counter = counter + 1

# 2. Using break to exit loop early
i = 0
while True:
    if i == 3:
        print("Breaking at", i)
        break
    print(i)
    i += 1

# 3. Using continue to skip to next iteration
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # skips printing 3
    print("x =", x)

# 4. while loop with else block
z = 0
while z < 3:
    print("z =", z)
    z += 1
else:
    print("Loop ended normally (no break)")

# 5. Infinite loop (be careful!)
# while True:
#     print("This runs forever")

# 6. Compound condition
n = 0
while n < 10 and n != 7:
    print(n)
    n += 2

# --------------------------------------------
# Counter update operators

# → counter += 1  → same as counter = counter + 1
# → counter -= 1  → same as counter = counter - 1
# → counter *= 2  → same as counter = counter * 2
# → counter /= 2  → same as counter = counter / 2

# Note:
# Python does NOT support the ++ or -- operators like other languages.
# Using x++ or x-- will cause a SyntaxError.
