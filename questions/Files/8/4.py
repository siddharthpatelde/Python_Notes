tab = {}

while True:
    user_input = input("Input: ").strip()

    if user_input == "Ende":
        print(tab)
        break

    parts = user_input.split()

    if len(parts) == 1:
        key = parts[0]
        if key in tab:
            print(tab[key])
        else:
            print("Unknown word")

    elif len(parts) == 2:
        key, value = parts
        tab[key] = value
        print("New entry")
