def myJoin(lst, sep):
    result = ""
    for i in range(len(lst)):
        result += lst[i]
        if i != len(lst) - 1:
            result += sep
    return result

mylist = ['Wir', 'müssen', 'uns', 'Sisyphos', 'als', 'einen', 'glücklichen', 'Menschen', 'vorstellen']
mystring = myJoin(mylist, '-')
print(mystring)
