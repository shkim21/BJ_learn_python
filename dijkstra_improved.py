import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())

INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]#빈 리스트 만들기(<-append를 위해서)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))#노드와 거리를 함께 저장(0:거리, 1:인접노드)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0            # 시작노드->시작노드 거리 기록. 같은 노드니깐 거리가 0임!
    
    while q:
        print("q:",q)
        dist, node = heapq.heappop(q)#가장 거리가 짧은(?)애를 뽑음
        print("dist:", dist, "node:", node)

        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[node] < dist:
            continue

        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in graph[node]:
            print("next:", next)
            cost = distance[node] + next[1]   # 시작->node거리 + node->node의 인접노드 거리   / next[1]: 비용?
            if cost < distance[next[0]]:      # cost < 시작->node의 인접노드 거리
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0])) #인접노드 추가


dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])