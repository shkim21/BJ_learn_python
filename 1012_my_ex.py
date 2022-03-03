T = int(input())

# field = [[0 for i in range(5)] for j in range(2)]

# print("filed:", field)
# field[1][1] = 1
# print("filed:", field)

for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    field = [[0 for i in range(N+2)] for j in range(M+2)]
    print("before filed:", field)
    for _ in range(K):
        X, Y = map(int, input().split())
        field[X+1][Y+1] = 1
    print("after field:", field)

    for i in range(1, M+1):#0, 1, 2,,,N-1
        for j in range(1, N+1): #0, 1, 2,,,M-1
            if field[i][j]:#1인 경우에 대해서
                print("i :", i, "j:",j)
                if field[i-1][j] or field[i][j-1] or field[i+1][j] or field[i][j+1]:
                    print("exist")
                    continue
                else:
                    print("else!")
                    cnt += 1
    print(cnt+1)


