day = input("Input: ").strip()

match day:
    case "Mo":
        print("Monday")
    case "Di":
        print("Tuesday")
    case "Mi":
        print("Wednesday")
    case "Do":
        print("Thursday")
    case "Fr":
        print("Friday")
    case "Sa":
        print("Saturday")
    case "So":
        print("Sunday")
    case _:
        print("Error")
