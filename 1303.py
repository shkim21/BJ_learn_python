from collections import deque
import copy

n, m = map(int, input().split())#가로, 세로

arr = []
for _ in range(m):#방법 찾아볼 것!
    ss = input()
    tmp = []
    tmp.extend(ss)
    arr.append(tmp)
# print("arr:",arr)

b_list = []
w_list = []

dx = [0,0, 1, -1]#상하좌우 움직임
dy = [1,-1, 0, 0]

visited = copy.deepcopy(arr)
# print("visited:", visited)#방문 여부 체크하는 배열

#bfs
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    cnt = 0
    visited[x][y] = 0# 왜 arr이 바뀌는 걸까,,,

    while queue:
        #경계값 내에서
        #가로세로 인접한 곳에 같은 값이 있는지
        v = queue.popleft()
        x_ = v[0]
        y_ = v[1]
        # print("x_, y_:", x_, y_)
        cnt += 1
        for i in range(4):
            nx = x_ + dx[i]#열
            ny = y_ + dy[i]#행
            if nx > m-1 or ny > n-1 or nx < 0 or ny <0:#경계값 처리
                continue

            # print("nx:", nx, "ny:", ny)
            # print("arr[x_][y_]:",arr[x_][y_])#arr[x_][y_]: 0 ??
            # print("arr:", arr)
            # print("visited:", visited)
            # print("arr[nx][ny]:", arr[nx][ny])
            # print("visited[nx][ny]:",visited[nx][ny])
            if arr[x_][y_] == arr[nx][ny] and visited[nx][ny] != 0:#같은 색깔일 때, 방문하지 않았을 때
                # print("same color")
                visited[nx][ny] = 0#방문처리
                queue.append([nx, ny])

    # print("cnt:", cnt)
    if arr[x][y] == 'W':
        w_list.append(cnt)
    else:
        b_list.append(cnt)

for i in range(m):
    for j in range(n):
        if visited[i][j] != 0:
            bfs(i, j)

# print("w_list:", w_list)
# print("b_list:",b_list)

s_w = 0
for w in w_list:
    s_w += w*w
# print(s_w)

s_b = 0
for b in b_list:
    s_b += b*b
print(s_w, s_b)


#graph = [list(input()) for _ in range(m)] 한줄로 입력 받는 법
#visited = [[False] * n for i in range(m)] 깊은 복사가 아니라 빈 리스트 선언하는 법