# Q4: Capitalized words in a sentence
sentence = input("Eingabe: ")
words = sentence.split()
capitalized = [word for word in words if word[0].isupper()]
print(capitalized)
