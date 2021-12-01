N, M = list(map(int, input().split()))

s = []#재귀함수를 이용하여 M개의 수열을 저장하기 위한 리스트

def dfs():
    if len(s)==M:#리스트에 들어간 수열들이 M개가 되면 리스트에 들어있는 숫자들 모두 출력하고 나옴
        print(' '.join(map(str,s)))
        return
    
    for i in range(1, N+1):#for문으로 1~N까지 숫자들 모두 확인
        if i not in s:#list s 중복여부 확인
            s.append(i)
            dfs()#가지치기하기. 재귀함수
            s.pop()

dfs()

# for i in range(N):#칸 3칸, 4칸,, 길이
#     s = []
#     for j in range(1, M+1):# 범위
#         # for k in range(1, M+1):
#         s.append(j)
#     print("s:", s)

#[1, 2, 3, 4]

# for i in range(1, N+1):
#     for k in range(M):
#         for j in range(1, N+1):
#             if i == j:
#                 pass
#             else:
#                 print(i, j)