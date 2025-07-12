# Q1: Count lines, words, and characters in automobil.txt
with open("automobil.txt", "r", encoding="utf-8") as file:
    content = file.readlines()

lines = len(content)
words = sum(len(line.split()) for line in content)
chars = sum(len(line) for line in content)

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", chars)
