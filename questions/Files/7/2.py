lst1 = [1, 3, 9, -11, 2, 0, 21]
lst2 = [2, 1, -2, 0, 3, -2, -11]

result = []
for i in range(len(lst1)):
    result.append(lst1[i] + lst2[i])

print("Result:", result)
