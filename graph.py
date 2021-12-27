class myGraph:
    def __init__(self):
        self.graph = {}

    def addInfo(self, startV, endVs):
        self.graph[startV] = endVs

    def addEdge(self, startV, endV):
        self.graph[V] = []

    def bfs(self, startV):
        q = [startV]
        visited = [startV]
        while q:
            #deque.popleft()
            nowV = q.pop(0)
            for nextV in self.graph[nowV]:
                if nextV not in visited:
                    q.append(nextV)
                    visited.append(nextV)
        return visited

    def dfs(self, startV):
        s = [startV]
        visited = []
        while s:
            nowV = s.pop()
            if nowV not in visited:
                visited.append(nowV)
                s.extend(self.graph[nowV][::-1])
        return visited

    def dfs_recursive(self, startV, visited=[]):
        visited.append(startV)

        for nextV in self.graph[startV]:
            if nextV not in visited:
                self.dfs_recursive(nextV, visited)

        return visited

g = myGraph()
g.addInfo('A', ['B', 'E', 'I'])

print(g.bfs('A'))