n = int(input())

Nlist = [0]*(n+1)

for i in range(1, n+1):#1, 2, 3,
    if i == 1:
        Nlist[i] = 1
    elif i == 2:
        Nlist[i] = 2
    else:
        Nlist[i] = Nlist[i-1]+Nlist[i-2]

# print("Nlist:", Nlist)

print(Nlist[n]%10007)


#DP 문제
#1. 테이블 정의 : D[i] : 2xi 직사각형을 나누는 방법수
#2. 점화식 세우기 조건 맞춰서.
#3. 초기값 설정(점화식에서 필요한 값들)