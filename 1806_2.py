n, s = map(int, input().split())

n_list = list(map(int, input().split()))

dp = [[0 for i in range(n)] for _ in range(n)]
ans = 100000

for i in range(n):
    dp[i][i] = n_list[i]

# print('dp:', dp)

for i in range(1, n):
    for j in range(0, i):
        dp[i][j] = dp[i-1][j] + dp[i][i]
        if dp[i][j] >= s:
            ans = min(ans, i-j+1)
# print("dp:",dp)
print(ans)

#메모리 초과 풀이....