N = int(input())

stairs = [0]*(N+2)
for i in range(N):
    a = int(input())
    stairs[i+1] = a

# print("stairs:", stairs)

score = [0]*(N+2) #리스트 범위 인덱싱 에러 안나도록
score[1] = stairs[1]
score[2] = stairs[1]+stairs[2]

for i in range(3, N+1):#1, 2, 3,,,

    score[i] = stairs[i]+ max(score[i-3]+stairs[i-1], score[i-2])#연속 3계단 방지(문제조건) 예외처리

# print("score:", score)
print(score[N])