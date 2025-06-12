words = set()

while True:
    entry = input("Input: ")
    if entry == "Ende":
        break
    words.add(entry)

print(words)
