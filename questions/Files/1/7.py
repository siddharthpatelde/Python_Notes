raw_input = input("Enter numbers: ")
numbers = [int(x.strip()) for x in raw_input.split(",")]

smallest = numbers[0]
largest = numbers[0]

for num in numbers[1:]:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest number:", smallest)
print("Largest number:", largest)
