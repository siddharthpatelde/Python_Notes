s = {'der', 'die', 'das', 'und', 'er', 'sie', 'es', 'du'}

while True:
    word = input("Input: ")
    if word == "Ende":
        break
    if word in s:
        s.remove(word)
        print("Removed")
    else:
        print("Not found")

print(s)
