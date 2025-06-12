import random

random.seed(0)
rolls = int(input("Rolls: "))
for _ in range(rolls):
    print(random.randint(1, 6))
