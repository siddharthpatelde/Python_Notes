# Q3: Raise and catch all exceptions, including custom ValueError
try:
    x = int(input("x = "))
    if x < 0:
        raise ValueError("Negative numbers not allowed")
    print("1/x =", 1/x)
except Exception as e:
    print(e)
