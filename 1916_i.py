import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 100000000

s = [[] for i in range(n + 1)] #빈리스트 저장
dp = [inf for i in range(n + 1)]#거리 저장

for i in range(m):
    a, b, w = map(int, input().split())
    s[a].append([b, w])#인덱스가 노드번호. 노드, 거리를 리스트로 저장함  노드가 첫번째로 와도 되나? 우선순위가 적용되나?

print("s:", s)

start, end = map(int, input().split())

def dijkstra(start):
    dp[start] = 0#start 초기화. 인덱스로 접근
    heap = []
    heappush(heap, [0, start])#우선순위 큐에 넣기

    while heap:#살짝 bfs랑 비슷 살짝
        w, n = heappop(heap)
        print("w:",w, "n:", n)

        if dp[n] < w:
            continue

        for n_n, wei in s[n]:# 선택한 노드의 인접노드와 거리 꺼내기
            n_w = w + wei#현재노드까지의 거리 + 인접노드까지의 거리 더함
            print("n_w:", n_w)
            if dp[n_n] > n_w: #거리가 더 작을 때
                dp[n_n] = n_w # 업데이트!
                heappush(heap, [n_w, n_n])#거리, 노드 순으로 순서를 바꿔서 넣음
                print("heap:", heap)#여기서 볼 땐 정렬 안되어 있는듯? 꺼낼 때만 잘 나오면 됨
                print("dp:", dp)

dijkstra(start)#start 노드로 시작

print("dp:", dp)#[100000000, 0, 2, 3, 1, 4]
print(dp[end])