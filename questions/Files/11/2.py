# Q2: Range with step 2 using list comprehension
start = int(input("start = "))
end = int(input("end = "))
result = [i for i in range(start, end+1, 2)]
print(result)
