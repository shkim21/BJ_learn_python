n, k = map(int, input().split())

dp = [[0 for _ in range(n)] for i in range(k)]
#dp[합되는 수][갯수]
print("dp:", dp)

for i in range(n): #0,1, ,,n-1
    dp[0][i] = 1
print("dp2:", dp)

for i in range(0, n):#가로줄
    for j in range(0, i): #0, 1, i-1
        dp[i][1] += dp[i-1][i-k]

#점화식 까지 생각했으나 [n][k]가 헷갈려서 집중을 제대로 하지 못햇음.
#3중 포문 형태가 나와서 더 하기를 멈췄는데 어떻게 해서든 했어야 했음.
#

#3중 포문 구현
n, k = map(int,input().split())
mod = 1000000000
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(1, k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][j-l]
        dp[i][j] %= mod
print(dp[k][n])


#점화식으로 간결해진 풀이
n, k = map(int, input().split())
mod = 1000000000

dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp[i][j] %= mod

print(dp[k][n])