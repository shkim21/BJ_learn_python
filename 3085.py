n = int(input())

arr =[[0 for _ in range(n)] for j in range(n)]

for i in range(n):
    ss = list(input())
    for j in range(len(ss)):
        arr[i][j] = ss[j]

# print("arr:", arr)

dx = [1, 0]#하, 우
dy = [0, 1]

def cal_max_len(arr):
    mx = 0
    # print("arr:", arr)

    n = len(arr[0])
    for i in range(n):
        for j in range(n):
            cnt = 1
            for k in range(j+1, n):
                if arr[i][j] == arr[i][k]:
                    cnt += 1
                else:
                    break
            mx = max(mx, cnt)#최대값 업데이트

    for j in range(n):#0, 1, 2,
        for i in range(n):#0, 1, 2,,
            cnt2 = 1
            for k in range(i+1, n):
                if arr[i][j] == arr[k][j]:
                    cnt2 += 1
                else:
                    break
            mx = max(mx, cnt2)

    # print("mx:",mx)
    return mx

res = 0

for i in range(n):
    for j in range(n):
        for k in range(2):
            # print("i:",i,"j:",j,"k:",k)
            tmp = [row[:] for row in arr]#deep copy 해야함...
            nx = i + dx[k]
            ny = j + dy[k]

            if nx <0 or nx > n-1 or ny < 0 or ny > n-1:#경계값 제한
                continue

            if tmp[i][j] == tmp[nx][ny]:#같을 때 패스
                continue
            else:
                # print("nx:",nx,"ny:",ny)
                # print("arr[nx][ny]:",arr[nx][ny])
                # print("arr[i][j]:", arr[i][j])
                # print("before tmp[i][j]:", tmp[i][j])
                # print("before tmp[nx][ny]:", tmp[nx][ny])
                tmp[i][j] = arr[nx][ny]#switch
                tmp[nx][ny] = arr[i][j]#스위치가 안 되는데?? 아니 왜 안됨?????? 리스트 만들때,,
                # print("after tmp[i][j]:", tmp[i][j])
                # print("after tmp[nx][ny]:", tmp[nx][ny])
                # print("tmp:", tmp)
            #tmp 검증하기! 최대 길이 계산하기
            r = cal_max_len(tmp)
            res = max(res, r)

# print("res:", res)

print(max(res))

#하... 시간초과