month = input("Input: ").strip().lower()

match month:
    case "mar" | "apr" | "may":
        print("Spring")
    case "jun" | "jul" | "aug":
        print("Summer")
    case "sep" | "oct" | "nov":
        print("Autumn")
    case "dec" | "jan" | "feb":
        print("Winter")
    case _:
        print("Error")
