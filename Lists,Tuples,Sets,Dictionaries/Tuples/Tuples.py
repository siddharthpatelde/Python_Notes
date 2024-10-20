#list example
List = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8']

#tuple example
Tuple = ('name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8')

#or

Tuple2 = 'name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8'


print(Tuple[0])

#you can not assign or change new value in Touples

#Tuple[0] = 'name2'

#just to make sure if the tuple is tuple

print(type(Tuple2))

#we just saw that we can not add any items to tuples but we can add two tuples together

tuple_1 = 1,2,3
tuple_2 = 'city','street','house'

tuple_3 = tuple_1 + tuple_2

print(tuple_3)

#we can not remove items in tuple, but we can permanently delete the tuple

del tuple_3
#print(tuple_3)


