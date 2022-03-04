from collections import deque

N = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maps = []

for _ in range(N):
    ss = list(map(int, input()))
    maps.append(ss)

# print("maps:", maps)
hap = []

def bfs(x, y):
    queue = deque()
    queue.append((x, y))#한번에 들어가나?
    # print("queue:", queue)
    a = 1
    maps[x][y] = 0#0으로 초기화!
    while queue:
        v = queue.popleft()
        # print("v:", v)
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            # print("nx:", nx, "ny:", ny)
            if nx <0 or nx >N-1 or ny<0 or ny>N-1:
                continue
            if maps[nx][ny]:
                # print("1 find")
                queue.append((nx, ny))
                maps[nx][ny] = 0
                a += 1
    return a
    
cnt = 0
for i in range(N):
    for j in range(N):
        if maps[i][j]:#1이면
            hap.append(bfs(i, j))
            cnt += 1
print(cnt)
hap = sorted(hap)
print(*hap, sep="\n")
