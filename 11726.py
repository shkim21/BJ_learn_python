n = int(input())

Nlist = [0]*(n+1)

for i in range(1, n+1):#1, 2, 3,
    if i == 1:
        Nlist[i] = 1
    elif i == 2:
        Nlist[i] = 2
    else:
        Nlist[i] = Nlist[i-1]+Nlist[i-2]

# print("Nlist:", Nlist)

print(Nlist[n]%10007)
