age = int(input("Please enter your age: "))

if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are of retirement age.")
