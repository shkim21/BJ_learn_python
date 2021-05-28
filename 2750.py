N = int(input())

s = []
for _ in range(N):
    a = int(input())
    s.append(a)

s.sort()
for sn in s:
    print(sn)