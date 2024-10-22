#let say we are making website like amazon and it has sevral key datas  like following

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