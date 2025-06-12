def total(n):
    if n <= 1:
        return n
    return n + total(n - 1)

n = int(input("n = "))
print("Sum =", total(n))
