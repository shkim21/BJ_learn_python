import heapq
import sys

def dijkstra(start):

    # 초기 배열 설정
    distances = {node: sys.maxsize for node in graph}
    print("distance:", distances)

    # 시작 노드의 거리는 0으로 설정
    distances[start] = 0
    queue = []# 빈 리스트 큐 선언. 여기다가 우선순위큐를 이용해서 담고 빼고 할꺼임

    # 시작 노드부터 탐색 시작 하기 위함. (거리, 노드) - 거리, 노드 순으로 넣은 이유는 heapq 모듈에 첫 번째 데이터를 기준으로 정렬을 진행하기 때문!! (노드, 거리) 순으로 넣으면 최소 힙이 예상한대로 정렬되지 않음
    heapq.heappush(queue, (distances[start], start))
    print("queue:", queue)# [(0, 'A')]

    # 우선 순위 큐에 데이터가 하나도 없을 때까지 반복
    while queue:
        # 가장 낮은 거리를 가진 노드와 거리를 추출
        current_distance, node = heapq.heappop(queue)
        print("current_distance:", current_distance, "node:", node)

        # 파이썬 heapq에 (거리, 노드) 순으로 넣다 보니까 동일한 노드라도 큐에 저장이 된다 예시: queue[(7, 'B'), (10, 'B')]
        # 이러한 문제를 아래 조건문으로 이미 계산되어 저장한 거리와 추출된 거리와 비교하여, 저장된 거리가 더 작다면 비교하지 않고 큐의 다음 데이터로 넘어간다.
        if distances[node] < current_distance:
            continue

        # 대상인 노드에서 인접한 노드와 거리를 순회
        for adjacency_node, distance in graph[node].items():#graph에 node를 키값으로 접근해서, items()로 딕셔너리에 있는 값들을 꺼냄!
            print("adjacency_node:", adjacency_node, "distance:", distance)
            
            # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더함!!
            weighted_distance = current_distance + distance#현재노드에 저장된 거리에 인접노드까지의 거리를 더함
            print("weighted_distance:", weighted_distance)

            # 배열에 저장된 거리보다 위의 가중치가 더 작으면 해당 노드의 거리 변경(업데이트!)
            if weighted_distance < distances[adjacency_node]:

                # 배열에 저장된 거리보다 가중치가 더 작으므로 변경
                distances[adjacency_node] = weighted_distance
                print("distances:", distances)

                # 다음 인접 거리를 계산 하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 다 저장함)
                heapq.heappush(queue, (weighted_distance, adjacency_node)) #자동으로 정렬시켜줌! 거리 작은 순으로!
                print("queue:", queue)

    return distances

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {'D': 9},
}

result = dijkstra('A')
print(result)#distances 반환됨

# {'A': 0, 'B': 7, 'C': 3, 'D': 9, 'E': 5}

#딕셔너리로, 튜플을 우선순위 큐에 넣고 뺌
#해당 큐를 인덱스로 접근해서 업데이트하는 방식이 아님 <- 여기서 살짝의 비효율성(?) 있을수도