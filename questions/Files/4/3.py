def rect(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

a = int(input("a = "))
b = int(input("b = "))

area, perimeter = rect(a, b)
print("Area =", area)
print("Perimeter =", perimeter)
