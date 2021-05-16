n = int(input())
a = n
for i in range(2, n+1):
    while a % i == 0:
        print(i)
        a = a // i