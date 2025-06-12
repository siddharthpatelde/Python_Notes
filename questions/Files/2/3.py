val = int(input("Value: "))

match val:
    case 0 | 1 | 2 | 3:
        print("Small number")
    case 4 | 5:
        print("Medium number")
    case 7 | 9:
        print("Special number")
    case _:
        print("Some other number")
