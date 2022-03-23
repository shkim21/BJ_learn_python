N = int(input())

#메모이제이션
memo = [0]*(N+1)

for i in range(2, N+1):#1, 2, 3,,,
    if i <= 3:
        memo[i] = 1
    else:
        temp = []
        if i % 3 == 0:#3의 배수. 3으로 나눴을 때
            temp.append(memo[i//3]+1)
        #2의 배수
        if i % 2 == 0:
            temp.append(memo[i//2]+1)
        temp.append(memo[i-1]+1)
        #-1일 때 
        #비교
        # print("temp:", temp)
        memo[i] = min(temp)

# print("memo:", memo)
ans = memo[N]
print(ans)


#DP 아이디어 : 뒤에서 앞으로 가야 한다!
#인덱스 안에서 연산 하는 아이디어
#이전 연산에서 1 횟수 늘려준 게 다음 연산임