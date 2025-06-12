sentence1 = input("Sentence 1: ")
sentence2 = input("Sentence 2: ")

set1 = set(sentence1.split())
set2 = set(sentence2.split())

print(set1 & set2)
