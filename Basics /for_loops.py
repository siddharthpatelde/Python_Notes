#for loops with strings
for letters in 'Math':
    print(letters)

# for loops with lists
grocery = ['milk','suger','oil','eggs']
for items in grocery:
    print(items)

#for loops with numbers
for i in [1,2,3,4,5]:
    print(i)

#for loops with range function
for i in range(20):
    print(i)


#more about range function
for i in range(10,20,2): #this means starts with 10 till 20 and skips 2 numbers
    print(i)
print("loop is done")

#how t add numbers with for loops
numbers = [1,2,3,4,5]
sum = 0
for i in numbers:
    sum = sum + i
print(f"Total: {sum}")
