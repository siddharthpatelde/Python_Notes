#create a function that greets the user
from functools import total_ordering


def greet(name):
    print(f"hello {name}, good day!!!")

# this function does some tasks and returns value
def add(num1, num2):
    return f"Total: {num1 + num2}"

greet("sid")
greet("john")
greet("boi")

print(add(10, 20))

#lets try ti save the value from our fuction in text file
#in order to put text in file
# step 1: create a text file
# step 2: save the result in the file
# step 3: closing the file

#step 1:
test_file = open("result.txt", "w") # open(name_of_file,w = write)
#step 2:
test_file.write(add(10,20))
#step 3:
test_file.close()



