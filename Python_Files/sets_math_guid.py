# SETS – MATHEMATICAL OPERATIONS

# We use sets to perform classic mathematical operations like:
# union, intersection, difference, symmetric difference, etc.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# --------------------------------------------
# 1. union() – combines both sets
print("Union:", a.union(b))       # {1, 2, 3, 4, 5, 6}
print("Using | :", a | b)

# 2. update() – adds elements from b to a
a1 = a.copy()
a1.update(b)
print("Update:", a1)

# --------------------------------------------
# 3. intersection() – common elements
print("Intersection:", a.intersection(b))  # {3, 4}
print("Using & :", a & b)

# 4. intersection_update() – keeps only common elements in a
a2 = a.copy()
a2.intersection_update(b)
print("Intersection Update:", a2)

# --------------------------------------------
# 5. difference() – items in a but not in b
print("Difference (a - b):", a.difference(b))  # {1, 2}
print("Using - :", a - b)

# 6. difference_update() – removes items in b from a
a3 = a.copy()
a3.difference_update(b)
print("Difference Update:", a3)

# --------------------------------------------
# 7. symmetric_difference() – elements in a or b but not both
print("Symmetric Difference:", a.symmetric_difference(b))  # {1, 2, 5, 6}
print("Using ^ :", a ^ b)

# 8. symmetric_difference_update() – modifies a to symmetric diff
a4 = a.copy()
a4.symmetric_difference_update(b)
print("Symmetric Difference Update:", a4)

# --------------------------------------------
# 9. issubset()
print("Is a subset of b:", a.issubset(b))  # False

# 10. issuperset()
print("Is a superset of b:", a.issuperset(b))  # False

# 11. isdisjoint()
x = {10, 20}
print("Is disjoint:", a.isdisjoint(x))  # True (no common elements)
