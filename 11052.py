N = int(input())

Plist = [0]+list(map(int, input().split()))

dp = [0 for i in range(N+1)]

# dp[0] = Plist[0]
# print("before dp:", dp)

for i in range(1, N+1):#1, 2, 3,,, N
    print("i:",i)
    for j in range(1, i+1):#1, 2, 3, i
        print("j:",j)
        # print("dp[i-j]+Plist[i-j]:", dp[i-1]+Plist[i-j])
        #dp[i] = max(Plist[i], dp[i-j]+Plist[i-j])
        dp[i] = max(dp[i], dp[i-j]+ Plist[j])
        print("dp:",dp)

print("after dp:", dp)

#dp[i]: 카드 i개를 구매하는 최대 가격
#p[k] = k개가 들어있는 카드팩 가격

