T = int(input())

dp = [1,1,1,2,2]

for j in range(5, 101):
    dp.append(dp[j-1]+dp[j-5])

# print("dp:", dp)
for i in range(T):
    N = int(input())
    print(dp[N-1])