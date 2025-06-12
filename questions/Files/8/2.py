tab = {'Mo': 1, 'Di': 2, 'Mi': 3, 'Do': 4, 'Fr': 5, 'Sa': 6, 'So': 7}

word = input("Input: ")
if word in tab:
    print(tab[word])
else:
    print("Unknown word")
