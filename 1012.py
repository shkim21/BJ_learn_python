from collections import deque

#1이 인접한 칸들을 연결하여 한 구역이라고 생각하기
#1인 칸 발견하면 BFS 수행. 1인 칸 0으로 변경. 1구역의 BFS 모두 끝나면 1이 모두 0으로 바뀜

#핵심 아이디어 : BFS를 수행할 때 인접 구역들을 모두 0으로 바꾼다! 몇번 BFS 수행했는지 세면 됨
#0으로 바꿔주는 것이 방문추가하는 것과 유사함

#이동하는 것을 배열로 나타내서 인덱스로 접근하며 이동함!
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()#데크로 큐 만듬
    queue.append((a, b)) #튜플 형태로 넣음
    graph[a][b] = 0#0으로 바꿈(방문추가한 것과 비슷!)

    #반복문
    while queue:
        x, y = queue.popleft()#항상 queue는 popleft함. 제일 먼저 넣은 부분 꺼냄
        for i in range(4):#0, 1, 2, 3
            #상하좌우 이동한 지점의 좌표
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:#경계값 처리. 범위 벗어날 때
                continue
            if graph[nx][ny] == 1: #인접한 부분이 1일 때
                graph[nx][ny] = 0 #0으로 바꾸고
                queue.append((nx, ny)) #큐에 삽입! while queue니깐 없어질 때까지 반복하게 됨!

    return

for i in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0 for i in range(m)] for j in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:#1일때 모두 bfs에 넣기!
                bfs(graph, a, b)#한 bfs 돌 때 인접한 부분들까지 모두 0으로 바꿔준다
                cnt += 1#카운트 하는 부분 위치!

    print(cnt)
