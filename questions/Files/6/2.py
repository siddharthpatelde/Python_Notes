from random import seed, choice

seed(0)
sentence = input("Input: ")
words = sentence.split()
print(choice(words))
