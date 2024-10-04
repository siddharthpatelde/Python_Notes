
#lets define a function with local variable

# def test_function():
#     test_num = 20
#     print(test_num)
#
# test_num = 30
# print(test_num)
# test_function()

# #lets create a simple function that adds two numbers
#
# def addition_number(num1,num2):
#     total = num1 + num2
#     return total
#
# result = addition_number(5,10)
# print(result)


x = 10
y = 5

def multiply():
    global x
    x = 10
    global y
    y = 20
    print(x*y)

multiply()
print("outside of functions: ",x*y)

