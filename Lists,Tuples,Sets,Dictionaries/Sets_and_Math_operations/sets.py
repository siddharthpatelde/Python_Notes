#sets are very similar data structure to list and tuples but lets see the major differences

#so lets say we have a list which has duplicates
#we can remove the duplicates using converting it to set

value = [1,2,2,3,4,5,5]
set = set(value)
print(set)

#second way of representing the sets is using {}
set2 = {2,2,3,4,}
print(set2)

#to remove stuff from your set you can either use

#remove mathod
set2.remove(3)
print(set2)

#but it will give error if you remove that's not in set
#set2.remove(50)

#so instead we use

#discard method
set2.discard(50)
print(set2)

#add method to add item
set2.add(50)
print(set2)
