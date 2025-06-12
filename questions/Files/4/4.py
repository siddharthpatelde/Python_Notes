def count_letter(s, letter):
    s = s.lower()
    letter = letter.lower()
    count = 0
    for char in s:
        if char == letter:
            count += 1
    return count

s = input("Input: ")
for vowel in "aeiou":
    print(f"{vowel}: {count_letter(s, vowel)}")
