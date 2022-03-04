N  = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]

for i in range(10):
    dp[0][i] = 1

# print("dp:", dp)

for i in range(1, N):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]

# print("after dp:", dp)
print(sum(dp[N-1])%10007)