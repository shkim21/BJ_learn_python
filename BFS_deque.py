from collections import deque

#유향 그래프 인듯?!
graph_list = {
    1:set([3, 4]),
    2: set([3, 4, 5]),
    3: set([1, 5]),
    4: set([1]),
    5: set([2, 6]),
    6: set([3, 5])
}
root_node = 1

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
        return visited

print(BFS_with_adj_list(graph_list, root_node))



def bfs(graph, start_node):#그래프와 시작노드
    visit = list()# 방문했던 노드 목록 저장. 순차적으로!
    queue = list() #다음으로 방문할 노드 목록 차례대로 저장할 리스트

    queue.append(start_node) #맨 처음 시작 노드 큐에 넣음

    while queue:#큐의 목록이 바닥날 때까지(더이상 방문할 노드가 없을 때까지)
        node = queue.pop(0)#큐의 맨 앞 노드 꺼내옴!(deque)
        if node not in visit:#해당 노드가 아직 방문 리스트에 없다면
            visit.append(node)#방문리스트에 추가
            queue.extend(graph[node])#해당 노드 자식 노드들 큐에 추가함!! graph의 키 값으로 접근 후 extend로 쪼갬!

    return visit

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}