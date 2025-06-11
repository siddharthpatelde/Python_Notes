# 2D LISTS AND NESTED LOOPS – FULL GUIDE

# A 2D list is a list of lists (matrix/grid style)

# Defining a 3x3 grid
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# --------------------------------------------
# 1. Accessing a specific element (row 0, column 0)
print("Top-left element:", num_grid[0][0])  # Output: 1

# 2. Accessing other positions
print("Middle element:", num_grid[1][1])    # Output: 5
print("Bottom-right:", num_grid[2][2])      # Output: 9

# --------------------------------------------
# 3. Iterating through 2D list using nested for-loops

# Outer loop goes over each row
for row in num_grid:
    # Inner loop goes over each column (element in that row)
    for column in row:
        print(column, end=" ")
    print()  # For new line after each row
