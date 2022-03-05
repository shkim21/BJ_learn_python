# from collections import deque

# N = int(input())

# #2차원 배열
# arr = [[0 for _ in range(2)] for _ in range(N)]

# print("arr:", arr)

# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     #방문처리!

#     while queue:
#         v = queue.popleft()
#         #0, 0
#         if 

# cnt = 0
# for i in range(N):
#     print("i:", i)
#     for j in range(2):
#         print("j:", j)
#         bfs(i, j)
#         cnt += 1


#DP, BFS 다 생각해봄
#각 칸에 사자가 있을 때 최대 경우의 수를 계산하고 다 더할 생각을 했음. 규칙을 발견하지 못했음.


#3가지 경우로 나뉘는 것을 캐치하지 못함.

#밑으로 배열을 추가하는 형태
#사자가 하나도 없을 때, 왼쪽에 사자가 있을 때, 오른쪽에 사자가 있을 때

# dp[n][0] : n 줄에 사자를 하나도 배치하지 않고 만들 수 있는 최대 수

# dp[n][1] : n 줄에 1열에 사자 하나 놓고 배치할 수 있는 최대 수

# dp[n][2] : n 줄에 2열에 사자 하나 놓고 배치할 수 있는 최대 수

n = int(input())

dp = [[0 for _ in range(3)] for j in range(n)]

dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1

# print("dp:", dp)
for i in range(1, n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901

# print("dp:", dp)
print(sum(dp[n-1])%9901)
