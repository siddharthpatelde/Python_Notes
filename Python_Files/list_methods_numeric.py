# LIST METHODS – NUMERIC LISTS ONLY

# These methods are especially useful and commonly used with lists that contain only numbers.

# Numeric list for demonstration
numbers = [5, 2, 8, 3, 5, 1, 8]

# 1. sort()
# → Sorts the list in ascending order (in-place)
numbers.sort()
print("sort():", numbers)  # [1, 2, 3, 5, 5, 8, 8]

# 2. reverse()
# → Reverses the list order in-place
numbers.reverse()
print("reverse():", numbers)  # [8, 8, 5, 5, 3, 2, 1]

# 3. count()
# → Counts occurrences of a specific number
print("count(5):", numbers.count(5))  # 2

# 4. max()
# → Returns the largest number in the list
print("max():", max(numbers))  # 8

# 5. min()
# → Returns the smallest number in the list
print("min():", min(numbers))  # 1

# 6. sum()
# → Returns the sum of all elements
print("sum():", sum(numbers))  # 32

# 7. average (manual)
# → Average = sum / count
average = sum(numbers) / len(numbers)
print("Average:", average)  # 4.571...

# 8. sorted()
# → Returns a new sorted list without modifying the original
original = [10, 3, 7]
sorted_list = sorted(original)
print("original:", original)       # [10, 3, 7]
print("sorted():", sorted_list)    # [3, 7, 10]
