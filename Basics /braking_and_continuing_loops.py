from os import system

system("clear")


# answer = 0
#
# while answer != 12:
#     if answer != 12:
#         answer = int(input("what is 4*3: "))
#         print("try again")
# print("correct answer")


# TRUE_ANS = 12
#
# while True:
#     ANS = int(input("what is 4*3: "))
#     if ANS == TRUE_ANS:
#         print("correct answer")
#         break


# program a code where you can enter three positive numbers
# but if you enter negative than breaks the loop
#
# for i in range(3):
#     num = int(input("Enter a number: "))
#
#     if num > 0:
#         continue
#     else:
#         break


# creat a program to print all the items in this list except
#'Orange' and 'Watermelon'

list = ["orange", 'mango', 'grapes', 'banana','watermelon']

for item in list:
    if item != "orange" and item != "watermelon":
        print(item)
