from os import system

system("clear")

#mathod one = insert
countries = ["usa","china","india","russia",'germany']

#insert takes two argument first is where to insert
#and second is what to insert
countries.insert(2,"new countries")
print(countries)

#now imagine you want to add new stuff at the end of list
countries.append("new countries")
print(countries)

#mathid two = remove
countries.remove("china")
print(countries)

#you can remove last item in list using pop()
countries.pop()
print(countries)

# #if what to remove all the items in list use clear()
# countries.clear()
# print(countries)

#mathod three = index (know the position of item)
print(countries.index("india"))
#index method is not so much preferable as it returns error if there is no matching item

print("italy" in countries)

##################################################################################

#workig with list of numbers

numbers = [10,5,7,3,1,9,5,2,0,1,3,1]

#sort method using sort()
numbers.sort()
print(numbers)

#count the numbers (how many times they appear)
print(numbers.count(1))

#sort in reverse direction
numbers.reverse()
print(numbers)

##################################################################################

#copy the list using copy() functions

countries = ["usa","china","india","russia",'germany']
countries2 = countries.copy()

countries.pop()

print(countries)
print(countries2)


#join the two lists togather using extend()

countries.extend(countries2)
print(countries)

#or
countries3 = ["brazil", "netherlands"]
countries3 = countries3 + countries2

print(countries)

#test edit



