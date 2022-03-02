N = int(input())

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