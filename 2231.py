N = int(input())

t = False

for M in range(1, N+1):
    a = 0
    l = len(str(M))
    a += M
    c = M
    for _ in range(l):
        a += c % 10
        c = c // 10
    if N == int(a):
        print(M)
        t = True
        break

if t == False:
    print("0")