com = int(input())
n = int(input())

graph = {key:[] for key in range(1, com+1)}
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print("graph:", graph)

visited = [False]*(com+1)

stack = []
def dfs(start):

    stack.append(start)
    visited[start] = 1

    #종료조건

    while stack:
        p = stack.pop()
        for i in graph[p]:
            if visited[i] == False:
                dfs(i)

dfs(1)

# print("visited:", visited)
cnt = 0
for i in visited[2:]:
    if i:
        cnt += 1

print(cnt)

###다른 풀이
visited2 = [0]*(n+1)

def dfs(start):
    global cnt
    visited2[start] = 1#방문처리
    for i in graph[start]:
        if visited2[i]==0:#방문하지 않았다면
            dfs(i)
            cnt +=1#카운트 늘리기