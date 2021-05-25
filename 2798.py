N, M = map(int, input().split())

a = list(map(int, input().split()))

l = len(a)
s = []
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            s.append(a[i]+a[j]+a[k])

c = []
for sn in s:
    if sn <= M:
        c.append(sn)

c.sort()
print(c[-1])
