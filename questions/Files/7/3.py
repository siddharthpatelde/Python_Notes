lst1 = [1, 3, 9, -11, 2, 0, 21]
lst2 = [2, 1, -2, 0, 3, -2, -11, 4, 8]

result = []
min_len = min(len(lst1), len(lst2))

for i in range(min_len):
    result.append(lst1[i] + lst2[i])

if len(lst1) > len(lst2):
    result += lst1[min_len:]
else:
    result += lst2[min_len:]

print("Result:", result)
