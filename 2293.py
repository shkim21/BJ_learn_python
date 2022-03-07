n, k = map(int, input().split())

# c_list = []

# for _ in range(n):
#     c = int(input())
#     c_list.append(c)

# for c in c_list:
#     #c 제외한 리스트
#     ex_c = c_list.remove(c)
#     max_c = k // c
#     for i in range(max_c):
#         tmp = k - i*c
#         # for e_c in ex_c:
            

#원래 나의 문제 풀이 발상 : 각각의 동전들 돌면서 갯수를 조합으로 구하기(리미트 : 최대로 나눌 수 있는 몫)
#뭔가 복잡해서 DP가 아닐까 의심 살짝 함. 어떻게 생각해야할지 방향을 잡지 못했음.
#DP의 핵심은 메모이제이션인데, 이전 단계와 다음 단계와의 관계를 파악하기 힘들었음.
#최대 몫까지 포문을 돌면서 가능한 갯수들을 조합으로 
#DP의 i를 어떻게 정의할 것인지.


#dp[3]은 dp[3] + dp[1] 인데, 이 얘기는 '1원짜리 동전으로 3원의 합을 만든 경우의 수(1+1+1)' + '1원짜리 동전으로 1원의 합을 만든 경우에 2를 더해서 만든 경우의 수(1+2)'라는 것이다.
#발상하는 것
#dp[3-2] 하는 이유는 2를 더하는 경우가 2를 더하지 않은 경우의 수와 같기 때문이다.

c = [int(input()) for i in range(n)]
dp = [0 for i in range(k+1)]
dp[0] = 1 #1개 뽑을 경우 처리하기 위함! 사소해보이지만 꼭 필요함!

for i in c:#1, 2, 5
    for j in range(i, k+1):#
        if j-i >=0:
            dp[j] += dp[j-i]
            # print("dp:", dp)

print(dp[k])