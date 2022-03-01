N = int(input())
Nlist = list(map(int, input().split()))
# Nlist.sort()
# print(Nlist)
M = int(input())
Mlist = list(map(int, input().split()))

a = []
for m in Mlist:
    if m in Nlist:
        a.append(str(1))
    else:
        a.append(str(0))

print(' '.join(a))