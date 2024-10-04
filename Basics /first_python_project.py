#python calculator programm
from os import system

#clear screen
system("clear")

#adding function
def addition(num1, num2):
    return num1 + num2

#substract function
def substraction(num1, num2):
    return num1 - num2

#multiply function
def multiplication(num1, num2):
    return num1 * num2

#devide function
def division(num1, num2):
    return num1 / num2


#prompting user to give an input
print("Select a math operation: \n"
      "1. Addition\n"
      "2. substraction\n"
      "3. multiplication\n"
      "4. division\n")

#taking input from the user

choice = int(input("Enter your choice: "))

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

if choice == 1:
    print(number_1,"+",number_2,"=",addition(number_1, number_2))

elif choice == 2:
    print(number_1,"-",number_2,"=",substraction(number_1, number_2))

elif choice == 3:
    print(number_1,"X",number_2,"=",multiplication(number_1, number_2))

elif choice == 4:
    print(number_1,"/",number_2,"=",division(number_1, number_2))

else:
    print("Invalid choice")
