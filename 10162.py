T = int(input())

A = T // 300 #5분 몫
B = (T - A*300) // 60
C = (T - A*300 - B*60) // 10

N = T - A*300 - B*60 - 10*C

if N != 0:
    print(-1)
else:
    print(A, B, C)