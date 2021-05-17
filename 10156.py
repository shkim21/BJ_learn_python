K, N, M = map(int, input().split())

p = K * N - M
if p < 0:
    print(0)
else:
    print(p)