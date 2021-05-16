N = int(input())

for i in range(N):
    num, st = input().split()
    num = int(num)
    #print(st[0])
    s = ''
    for j in range(len(st)):
        s += st[j] * num
    print(s)
