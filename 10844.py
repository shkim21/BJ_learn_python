# N = int(input())

dp = [9]
sub = [1, 2]

# for i in range(1, N):#1
#     a = dp[i-1] - sub[i-1]
#     # print("a:", a)
#     s = a * 2
#     s += sub[i-1]
#     # print("s:",s)
#     sub.append(sub[i-1]+sub[i])
#     dp.append(s%1000000000)

# print(dp[N-1])

#틀린 풀이 시도 : 없는 규칙을 찾으려 했다. 편법으로.
#DP인 거는 알았는데 합 숫자를 저장하는 형태로 구현함.

#DP! 2차원 리스트 쓰는 경우 많다!
#dp테이블은 이차원 리스트이며 dp[자리 수][앞에 오는 숫자]=경우의 수이다.

N = int(input())

dp = [[0]*10 for _ in range(N+1)]
# print("first dp:", dp)

#첫번째 배열 만들어줌. 초기값 세팅
for i in range(1, 10):#1~9
    dp[1][i] = 1
# print("two dp:", dp)

for i in range(2, N+1):
    print("i:", i)
    for j in range(10):#0, 1, ,,, 9
        if j == 0:
            dp[i][j] = dp[i-1][1] #이전 숫자 1만 0이 될 수 있음. 그대로 들어감
        elif j == 9:
            dp[i][j] = dp[i-1][8] #이전 숫자 8만 9가 될 수 있음
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]#그외의 경우(1~8)엔 그전 숫자가 1 작은 경우와 1 큰 경우의 합이 들어감
    print("dp:", dp)
print(sum(dp[N])% 1000000000)

#대각선 합 -> dp로 업데이트!
#점화식!

#계단수 자리와 끝나는 숫자 함께 고려한 2차원 배열