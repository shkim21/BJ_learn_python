n = int(input())
c = 100
s = 100
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        s -= a
    elif a < b:
        c -= b

print(c)
print(s)
