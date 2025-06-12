total = 0

while True:
    line = input("Input: ").strip()
    if line == "":
        break
    for num in line.split():
        total += int(num)

print("Sum:", total)
