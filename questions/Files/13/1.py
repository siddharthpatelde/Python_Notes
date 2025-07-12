# Q1: Reciprocal with ZeroDivisionError handling
try:
    x = int(input("x = "))
    print("1/x =", 1/x)
except ZeroDivisionError:
    print("Division by 0 not allowed")
