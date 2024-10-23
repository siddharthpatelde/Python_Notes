#let say we are making website like amazon and it has sevral key datas  like following
from os import system

#Online order

#item_type = "phone"
#manufacturer = "apple"
#seller = "tech-world"
#year = 2024
#item_id = (20.453, 12.123)

#now lets create the python dictionary
order = {"item_type": "phone", "manufacturer": "apple",
         "seller": "tech-world", "year": 2024, "item_id": (20.453, 12.123)}
print(type(order)) #verify that our order is of type dictionary

# Second way to defining the Dictionary in python is using dict() function
order2 = dict(type = "laptop", manufacturer = "apple", year = 2024, ram = 32)
print(order2)

#add additional elements to our dictionary using brackets
order2["order_number"] = 234124
order2["order_id"] = "45645342"
print(order2)

#accsessing the data from dictionary
print(order2["order_number"])
#print(order2["order"]) in this case we will get error

#to prevent key error we can use try or n operator

if 'age' in order2:
    print(order2['age'])
else:
    print("the key value not found in dictionary")

#or using try

try:
    print(order2['age'])
except KeyError:                                        #type of error
    print("the key value not found in dictionary")

#lets print all the data in dictorary
for key in order2:
    print(f"{key}: {order2[key]}")

#in order to see what you can do with dictionary do this first
print(dir(order2))

#output may look like this:['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
#                           '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
#                            '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__',
#                            '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__',
#                            '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
#                            '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
#                            'popitem', 'setdefault', 'update', 'values']

#to see how any method works use help() function

#help(order2.get)

check_age = order2.get("age", "age was not specified")
print(check_age)
