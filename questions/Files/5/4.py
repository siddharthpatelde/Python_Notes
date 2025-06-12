total = 0

while True:
    line = input("Input: ").strip()
    if line == "":
        break
    total += int(line)

print("Sum:", total)
