from collections import deque

N, M, V = map(int, input().split())#V : start point 

s = []
visited = [False]*(N+1)

def bfs():
    pass

graph = {i : [] for i in range(1, N+1)}
# print("graph:", graph)
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

s.append(V)

def dfs(start, graph):
    # print("start:", start)
    # print("graph:", graph)
    # print("s:", s)
    print(start, end=' ')
    visited[start]= True

    # if len(s) == N:#종료조건이 잘못됨!
    #     print(*s)
    #     return
    
    for i in graph[start]:
        # print("I:", i)
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(i, graph)
            # visited[i] = False
            s.pop()
    return

# dfs(V, graph)
# print()
s2 = []

visited_bfs = [False]*(N+1)

def bfs(graph, start, visited):
    # print("graph:", graph)
    # print("start:", start)
    # print("visited:", visited)
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        s2.append(v)
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # bfs(graph, i, visited)
    return s2

result = bfs(graph, V, visited_bfs)
# print(*result)


#다른 사람 풀이!

#DFS : 스택과 재귀

def dfs2(n):
    print(n, end=" ")#연속 출력. 화면에만 뜨면 되니깐. 따로 저장할 필요x
    visited[n] = True#방문 추가
    for i in graph[n]:
        if not visited[i]:#방문하지 않았을 땐 dfs 재귀!
            dfs(i)

#BFS : 큐
def bfs2(n):
    visited[n] = True #방문추가
    queue = deque([n]) #큐 만들기

    while queue:
        v = queue.popleft()#앞쪽에서부터 빼기
        print(v, end=' ')#출력
        for i in graph[v]:
            if not visited[i]:#방문하지 않았으면
                queue.append(i)#큐에 추가!
                visited[i] = True
        
graph3 = [[] for _ in range(N+1)]#이중 리스트 사용
visited3 = [False] * (N + 1)



def bfs_my(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print("queue:", queue)

    while queue:
        pop = queue.popleft()##popleft!!
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited_my = [False]*(N+1)
bfs_my(graph, V, visited_my)