import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

costs = {}
graph = {k:[] for k in range(1, n+1)}#빈 리스트 만들어서 업데이트!

for _ in range(m):
    start, end, cost = map(int, input().split())
    print(start, end, cost)
    costs[(start, end)] = cost
    costs[(end, start)] = cost
    print("costs:",costs)#costs: {(1, 2): 2, (2, 1): 2}
    graph[start].append(end)
    graph[end].append(start)
    print('graph:', graph)

s_node, e_node = map(int, input().split())

ans = []
stack = []
res = 0
visited = [False]*(n+1)

def dfs(start, pre, res):
    print("start:", start, "pre:",pre,"res:",res)

    if start == e_node:#종료조건
        # res += costs[(start, pre)]
        ans.append(res)
        res = 0#-= costs[(start, pre)]
        return

    stack.append(start)
    visited[start] = True

    if stack:
        v = stack.pop()
        for j in graph[v]:#2, 3
            if not visited[j]:
                res += costs[(start, j)]#1, 
                dfs(j, start, res)


dfs(s_node, None, res)
print("ans:", ans)

#res 돌아갈 때 초기화를 어디서 해주어야 하는가,,,