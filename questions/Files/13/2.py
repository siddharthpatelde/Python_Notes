# Q2: Handle ZeroDivisionError and ValueError
try:
    x = int(input("x = "))
    print("1/x =", 1/x)
except ZeroDivisionError:
    print("Division by 0 not allowed")
except ValueError:
    print("Please enter a number")
