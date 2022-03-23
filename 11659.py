import sys
input = sys.stdin.readline
# print = sys.stdout.write

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
# print("n_list:", n_list)
dp = [0]*(n+1)
# dp[1] = n_list[0]
for i in range(1, n+1):
    dp[i] = dp[i-1] + n_list[i-1]
# print("dp:",dp)
for _ in range(m):
    i, j = map(int, input().split())
    print(str(dp[j]- dp[i-1]))