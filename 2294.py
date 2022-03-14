n, k = map(int, input().split())

coins = []#list(map(int, input().split()))

for _ in range(n):
    coins.append(int(input()))

#점화식을 모르겠다.
#dp 메모이제이션 리스트를 어떻게 정의할 것인지 모르겠다.

#리스트 인덱스 : 그 숫자를 만들기 위한 최소 갯수

#범위 : 1~k까지. for문 돌아야 함.
#코인 돌면서 코인으로 조합할 수 있는 숫자 인덱스로 접근해서 숫자 업데이트 해야함
#min?

dp = [0]*(k+1)

# for i in range(1, k+1):
#     for coin in coins:
#         dp[coin] = 1




# 로직
# 1. 데이터들을 1차원 배열에 담는다.
# 2. 최소 코인 갯수를 저장할 dp배열을 만들고 max(10001)으로 초기화시켜준다.
# 3. 코인 배열의 값을 가져오고
# 4. 그 값만큼 올리면서 for문을 돌아주는데
# 5. 현재 값에서 가져온 코인 값을, 빼주었을 때의 코인 사용 개수에 지금 코인 개수 하나를 더한 값과, 이전 코인들로만 조합했을 때 사용된 코인 개수를 비교하여 더 작은 값을 dp배열에 담는다.


# for num in coins:
#     for i in range(num, k+1):#범위 지정이 핵심!
#         dp[i] = min(dp[i], dp[i-num]+1)
#     if dp[k] == 10001:
#         print(-1)
#     else:
#         print(dp[k])


# dp의 점화식은 dp[i] = min(dp[i - coin]) + 1 이 될 수 있다.
# 즉 dp[i]에는 dp[i - 1], dp[i - 5], dp[i - 12]중 가장 작은 값에 1을 더해주면 된다.
# 조건은 i가 coin보다 크거나 같아야 하고, -1이 아니어야 한다.

for i in range(1, k + 1):#1부터 k까지  dp[i] 는 숫자 i를 만들기 위한 최소 동전개수
    a = []#빈리스트
    print("dp:", dp)
    for j in coins:#각 코인들 돌면서
        if j <= i and dp[i - j] != -1:#이 조건을 어떻게 생각함...??
            a.append(dp[i - j])
    print("a:", a)
    if not a:#a가 비어 있으면
        dp[i] = -1
    else:# 만든 a 리스트 중 최소값에 1 더하기
        dp[i] = min(a) + 1

print(dp[k])


# 15원을 만들고 싶어
# 그러면
# 14원에서 1원을 더하거나, 10원에서 5원을 더하거나, 3원에서 12원을 더하거나


#어떤 수 x를 만들기 위해선, 지금 가지고 있는 동전들 중에서 동전의 가치를 뺀 수 에서 동전의 가치만큼 더해야 x를 만들 수 있다.
#점화식 관계. i 번째와 i-1번째? 나 이전 단계를 생각해보기