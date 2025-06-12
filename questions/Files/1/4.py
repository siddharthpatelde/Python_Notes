a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
