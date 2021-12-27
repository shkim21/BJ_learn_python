graph_list = {
    1: set([3, 4]),
    2: set([3, 4, 5]),
    3: set([1, 5]),
    4: set([1]),
    5: set([2, 6]),
    6: set([3, 5])
}

root_node = 1

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


print(DFS_with_adj_list(graph_list, root_node))


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()#맨 마지막에 넣었던 아이템 가져옴
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

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

def DFS2(start_node):

    # 1) stack에 첫번째 노드 넣으면서 시작
    stack = [start_node, ]

    while True:
        #2) stack이 비어있는지 확인
        if len(stack) == 0:
            print("all node searched.")
            return None

        #stack이 비어있지 않다면
        #3) stack에서 맨 위 노드를 pop
        node = stack.pop()

        #꺼낸 노드가 target인지 확인
        #4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print("The target found.")
            return node

        #5) node의 자식을 expand 해서 children에 저장
        children = expand(node)

        #6) children을 stack에 쌓기
        stack.extend(children)

