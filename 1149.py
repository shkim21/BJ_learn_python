# N = int(input())

# s = []
# hap = []

# visited = [False]*(N+1)#방문여부

# def dfs(start):
#     #종료조건
#     print("start:", start)
#     if len(s) == 3:
#         hap.append(sum(s))
#         print("hap:", hap)
#         return

#     for i in range(start, N+1):#1, 2, 3,,,
#         #2번집
#         print("i:", i)
#         if not visited[i]:#방문 안했을 때
#             for idx, j in enumerate(graph[i]):#30, 19, 5
#                 print("idx:", idx)
#                 print("j:", j)
#                 if visited[i-1] == idx:#false와 0이 같아짐,, 이전에 방문했던 거 체크,,
#                     continue
#                 s.append(j)
#                 visited[i] = idx
#                 print("vistied:", visited)
#                 dfs(i+1)
#                 print("s:", s)
#                 # visited[i] = False
#                 s.pop()
                

# graph = {}

# for i in range(N):
#     r, g, b = map(int, input().split())
#     graph[i+1] = [r, g, b]

# print("graph:", graph)
# dfs(1)

#나의 문제 아이디어 : 각각의 모든 경우를 계산해서 최솟값 구하기
#DP로 풀수 있는 조건들을 생각하지 못햇음.
#가지치기로 모든 경우 돌려봐야 한다고 생각함... 무엇을 방문했는지 저장해야 되고 피해가야하는 부분에서 막힘
#실버1에 쫄아서 문제 조건이 까다롭다고 생각함. DP 하기에 복잡하다고 지레 겁먹음.


#풀이
#현재 집에서 각각 색을 칠했을 때의 가장 적은 비용을 저장해서 재사용하는 것을 중점으로 둬야한다.

import sys
read = sys.stdin.readline

N = int(read())
cache = [list(map(int, read().split())) for _ in range(N)]#2차원 배열에 바로 집어넣기!
print("cache:", cache)

#같은 색을 연달아 칠할 수 없으므로 만약에 현재 빨간색이면, 이전 초록, 파란색 비용 중 작은 비용으로 선택
for i in range(1, N):#1, 2, 3, 두번째 부터 시작!
    print("i:", i)
    cache[i][0] += min(cache[i-1][1], cache[i-1][2])#0번째는 이전 집의 첫번째 두번째 집 중 최소값!
    cache[i][1] += min(cache[i-1][0], cache[i-1][2])
    cache[i][2] += min(cache[i-1][0], cache[i-1][1])
    print("cache:", cache)
#초기 데이터 집어 넣고 업데이트 시키는 방식

#가장 마지막 집(이때까지의 합이 들어가 있음)의 최소값
print(min(cache[-1]))

#이전까지의 합을 이용한다는 점에서 DP문제!