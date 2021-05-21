T = True

while T:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        T = False
        continue
    print(a+b)