n = int(input())

t = True
dp = [0]*(n+1)
#dp[i] : i를 1로 만드는 방법 수
dp[1] = 0
# dp[2] = 1
# dp[3] = 1
m = n

while t:
    print("n:", n)
    dp[n] = dp[n-1] + 1
    if n % 3 == 0:
        dp[n] = min(dp[n//3] + 1, dp[n])
        n = int(n//3)
        continue
    if n % 2 == 0:
        dp[n] = min(dp[n//2] + 1, dp[n])
        n = int(n//2)
        continue
    if n == 1:
        print("dp:", dp) #dp[m]
        break
    n -= 1