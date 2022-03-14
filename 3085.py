n = int(input())

# arr =[[0 for _ in range(n)] for j in range(n)]
arr = []

for i in range(n):
    ss = list(map(str, input()))
    arr.append(ss)
    # for j in range(len(ss)):#이중포문
    #     arr[i][j] = ss[j]

# print("arr:", arr)

dx = [1, 0]#하, 우
dy = [0, 1]

def cal_max_len(arr):
    mx = 0
    # print("arr:", arr)

    n = len(arr[0])
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            # for k in range(j+1, n):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
            else:
                break

            mx = max(mx, cnt)#최대값 업데이트

    for j in range(n):#0, 1, 2,
        cnt2 = 1
        for i in range(n-1):#0, 1, 2,,
            # for k in range(i+1, n):
            if arr[i][j] == arr[i+1][j]:
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
            # tmp = arr[:]#[row[:] for row in arr]#deep copy 해야함...
            nx = i + dx[k]
            ny = j + dy[k]

            if nx <0 or nx > n-1 or ny < 0 or ny > n-1:#경계값 제한
                continue

            if arr[i][j] == arr[nx][ny]:#같을 때 패스
                continue
            else:
                # print("nx:",nx,"ny:",ny)
                # print("arr[nx][ny]:",arr[nx][ny])
                # print("arr[i][j]:", arr[i][j])
                # print("before tmp[i][j]:", arr[i][j])
                # print("before tmp[nx][ny]:", arr[nx][ny])
                arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]#switch
                # = #스위치가 안 되는데?? 아니 왜 안됨?????? 리스트 만들때,,
                # print("after tmp[i][j]:", arr[i][j])
                # print("after tmp[nx][ny]:", arr[nx][ny])
                # print("tmp:", arr)
                #tmp 검증하기! 최대 길이 계산하기
                r = cal_max_len(arr)
                res = max(res, r)
                arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]

# print("res:", res)

print(res)

#하... 시간초과
#for문이 너무 많았음.

#행마다 같은 색이 있는 경우/ 열마다 같은 색이 있는 경우 나눠서 계산하기

#3중 포문을 쓰기 보다 다음 것(+1) 과 비교해서 체크가능