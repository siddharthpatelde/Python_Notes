#lets creat 2D list and see how it looks lile

num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(num_grid[1][1])

#or using for loop
for row in num_grid:
    for cell in row:
        print(cell)