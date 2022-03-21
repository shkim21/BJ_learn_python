from collections import deque
import copy

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
# print("arr:",arr)
values = copy.deepcopy(arr)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append([0, 0])
    arr[0][0] = 0#방문처리

    while queue:
        x, y = queue.popleft()
        # print("x:",x, "y:",y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #중복처리 해줘야 함
            #경계값 처리
            if nx > n-1 or nx < 0 or ny > m-1 or ny < 0:
                continue
            
            if arr[nx][ny]:
                # print("1 nx, ny:", nx, ny)
                arr[nx][ny] = 0
                values[nx][ny] = values[x][y] + 1
                queue.append([nx, ny])

bfs()

# print("arr:",arr)
# print("values:", values)
print(values[n-1][m-1])

#한방에 맞춤! 20분 컷
#방문처리 하는 부분에서 deepcopy가 필요하지 않았음.. 빈 리스트 만들고 거기에 저장해도 괜찮았을듯