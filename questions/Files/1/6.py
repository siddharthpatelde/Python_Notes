age = int(input("Please enter your age: "))

if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
elif age <= 99:
    print("You are of retirement age.")
else:
    print("You are in the Methuselah age group.")
