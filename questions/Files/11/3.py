# Q3: Numbers from 1 to N not divisible by 3
N = int(input("N = "))
filtered = [i for i in range(1, N+1) if i % 3 != 0]
print(filtered)
