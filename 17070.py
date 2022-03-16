n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
print("arr:",arr)

stack = []
cnt = 0

def dfs(position, tuples):

    stack.append([position, list(tuples)])

    #종료조건
    if tuples[0] == n-1 and tuples[1] == n-1:
        cnt += 1
        return

    while stack:
        print("stack:", stack)
        v = stack.pop()

        pos = v[0]
        x = int(v[1][0])#행
        y = int(v[1][1])#열
        print("pos:", pos, "x:", x, "y:", y)

        #경계값, 도착지점

        if x + 1 > n or y + 1 > n:
            continue
        
        if pos == 'r':#오른쪽이동
            print("arr[x, y+1]:", arr[x][y+1])
            if arr[x][y+1] != 1:#다음 열이 1이 아니면
                # stack.append(['r', tuple(x, y+1)])
                dfs('r', [x, y+1])
                stack.pop()

            if arr[x][y+1] != 1 and arr[x+1][y+1] != 1 and arr[x+1][y] != 1:
                # stack.append(['a', tuple(x+1, y+1)])
                dfs('a', [x+1, y+1])
                stack.pop()


        elif pos == 'd':#아래로 이동
            if arr[x+1][y] != 1:
                # stack.append(['d', tuple(x+1, y)])
                dfs('d', [x+1, y])
                stack.pop()
            if arr[x][y+1] != 1 and arr[x+1][y] != 1 and arr[x+1][y+1] != 1:
                # stack.append(['a', tuple(x+1, y+1)])
                dfs('a', [x+1, y+1])
                stack.pop()

        else:#'a' 대각선 이동
            if arr[x][y+1] != 1:
                # stack.append(['r', tuple(x, y+1)])
                dfs('r', [x, y+1])
                stack.pop()
            if arr[x+1][y] != 1:
                # stack.append(['d', tuple(x+1, y)])
                dfs('d', [x+1, y])
                stack.pop()
            if arr[x+1][y] != 1 and arr[x][y+1] !=1 and arr[x+1][y+1] != 1:
                # stack.append(['a', tuple(x+1, y+1)])
                dfs('a', [x+1, y+1])
                stack.pop()


dfs('r', [0, 1])

print("cnt:", cnt)
# for i in range(n):
#     for j in range(n):
