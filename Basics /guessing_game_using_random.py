import random
from os import system

#random.randit(a,b) generates random integer number between a to b
random_number = random.randint(1,9)
guess_count = 3

system('clear')
for i in range(guess_count):
    guess = int(input("Guess a number between 1 and 9: "))
    if random_number == guess :
        print("You got it right!")
        break
    print(f"Wrong guess!, {guess_count - i - 1} Try remaining")
    if i >= 2:
        print("Game Over")

