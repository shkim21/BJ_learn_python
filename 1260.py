import collections

N, M, V = map(int, input().split())
graph = {}

for i in range(M):
    start, end = map(str, input().split())
    #그래프 키 : start, value : end set
    # graph[start] = end
    if start in graph.keys():#graph[start]:#이미 있는 값이 경우
        graph[str(start)].add(end)
    else:
        graph[str(start)] = set(end)

print("graph:", graph)