lst = [1, 3, 9, -11, 2, 0, 21]

for i in range(len(lst)):
    min_index = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print("Result:", lst)
