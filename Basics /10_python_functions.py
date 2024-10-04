from os import system

system('clear')
string1 = 'today we will be Having loOk at Capitalize function'

#capitalize()
print(string1.capitalize())

#lower()
print(string1.lower())

#title()
print(string1.title())

#casefold() - works like lower() but more stronger
print(string1.casefold())

#upper()
print(string1.upper())

#count('string', start, end) - start/end is for finding 'string' in given range
print(string1.count('be'))

list1 = [1,2,3,4,5,6,9,9,10]

print(list1.count(9))

#find() - works like count() but gives position
string2 = "when was the letter 'a' first mentioned?"
print(string2.find('a'))

#len() - gives length of the string
print(len(string1))
print(len(string2))

#replace(oldvalue,newvalue,how many times)
string3 = "well you be able to finish this task?"
print(string3.replace('well','will',1))

#swapcase() - replacese lower case with upper and viseversa
string4 = 'hELLO, hOW ARE YOU DOING?'
print(string4.swapcase())

#join()
Tuple1 = ('hello','world','how','are','you','doing')
string5 = '_'.join(Tuple1)
string6 = ' '.join(Tuple1)

print(string5)
print(string6)

