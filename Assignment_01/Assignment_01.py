cars = [
{'car': 'Mitsubishi', 'year': 2004, 'price': 12000},
{'car': 'Ford', 'year': 2002, 'price': 14000},
{'car': 'BMW', 'year': 2017, 'price': 45000},
{'car': 'Mercedes', 'year': 2008, 'price': 18000},
{'car': 'Audi', 'year': 2005, 'price': 16000},
{'car': 'VW', 'year': 2012, 'price': 32000},
{'car': 'Toyota', 'year': 2011, 'price': 36000},
{'car': 'Toyota', 'year': 2011, 'price': 36000},
{'car': 'Maserati', 'year': 2020, 'price': 65000},
{'car': 'Porsche', 'year': 2021, 'price': 120000},
{'car': 'Hyundai', 'year': 2022, 'price': 45000},
]

print("How would you like to sort the list?")
print("(a) based on price")
print("(b) based on year")
print("(e) to exit")

case = (input("choose "))

while case != 'e':
    if case == 'a':
        price_sorted = sorted(cars, key=lambda x: x['price'], reverse=False)
        print(price_sorted)
    elif case == 'b':
        year_sorted = sorted(cars, key=lambda x: x['year'], reverse=False)
        print(year_sorted)
    else:
        print("invalid input")
    print("How would you like to sort the list?")
    print("(a) based on price")
    print("(b) based on year")
    print("(e) to exit")
    case = (input("choose "))

