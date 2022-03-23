n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# print("arr:",arr)

tmp = 0
tmps = 1001
for j in range(3):
    visited = [-1]*(n+1)#방문한 인덱스 저장
    tmp = arr[0][j]
    visited[0] = j
    for i in range(1, n):
        idxs = [0, 1, 2]
        pre_i = visited[i-1]
        # print("pre_i:",pre_i)
        idxs.remove(pre_i)
        x, y = idxs
        mm = min(arr[i][x], arr[i][y])
        if arr[i][x] > arr[i][y]:
            visited[i] = y
        else:
            visited[i] = x
        tmp += mm
    # print("visited:", visited)
    # print("tmp:", tmp)
    tmps = min(tmps, tmp)

print(tmps)

#나의 시도 : visited 방문한 인덱스를 저장해서, 그 값을 제외하고 다른 두 인덱스 중 최소값을 찾아서 더해가는 방식
#예제를 통과하지 못했음.. 모든 경우를 고려하지 못하기 때문임

###!!! DP 아이디어 : 고려해야할 조건이 2개 이상일 때, n차원 배열로 n개의 조건을 다루는 것을 생각하라!
#D[i][0] : i번째 집까지 칠할 때 비용의 최솟값, 단 i번째 집은 빨강

