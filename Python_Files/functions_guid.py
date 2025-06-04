# FUNCTIONS – FULL USAGE GUIDE

# Basic Syntax:
# def function_name(parameters):
#     block of code

# --------------------------------------------
# 1. Defining a basic function
def greet():
    print("Hello from the function!")

# Call the function AFTER defining it
greet()

# --------------------------------------------
# 2. DOs and DON'Ts
# Don't call a function before it's defined:
# greet()  # This would raise NameError if called before definition

# Always define before calling:
def welcome():
    print("Welcome to Python!")

welcome()

# --------------------------------------------
# 3. Function that performs a task (prints something)
def print_sum(a, b):
    print("The sum is:", a + b)

print_sum(4, 5)  # Output: The sum is: 9

# --------------------------------------------
# 4. Function that calculates and returns a value
def get_sum(a, b):
    return a + b

result = get_sum(10, 20)
print("Returned sum:", result)

# --------------------------------------------
# 5. Local vs Global Variables

# Global variable
counter = 100

def increase_counter():
    # Local variable (does not affect global counter)
    counter = 0
    counter += 1
    print("Local counter:", counter)

increase_counter()
print("Global counter remains:", counter)

# --------------------------------------------
# 6. Using 'global' keyword to modify global variable
count = 0

def modify_global():
    global count
    count += 1
    print("Modified global count:", count)

modify_global()
print("Global count after function:", count)
