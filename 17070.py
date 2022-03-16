n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
# print("arr:",arr)

stack = []
cnt = 0

def dfs(position, tuples):

    global cnt
    #종료조건
    if tuples[0] == n-1 and tuples[1] == n-1:
        cnt += 1
        return

    pos = position
    x = tuples[0]#행
    y = tuples[1]#열
    
    if pos == 'r':#오른쪽이동
        if y + 1< n and arr[x][y+1] != 1:#다음 열이 1이 아니면
            dfs('r', [x, y+1])
        if y + 1 < n and x + 1 < n:
            if arr[x][y+1] != 1 and arr[x+1][y+1] != 1 and arr[x+1][y] != 1:
                dfs('a', [x+1, y+1])

    elif pos == 'd':#아래로 이동
        if x + 1 < n and arr[x+1][y] != 1:
            dfs('d', [x+1, y])
        if x + 1 < n and y + 1 < n:
            if arr[x][y+1] != 1 and arr[x+1][y] != 1 and arr[x+1][y+1] != 1:
                dfs('a', [x+1, y+1])

    else:#'a' 대각선 이동
        if y+ 1 < n and arr[x][y+1] != 1:
            dfs('r', [x, y+1])
        if x+ 1< n and arr[x+1][y] != 1:
            dfs('d', [x+1, y])
        if x+1<n and y+1<n:
            if arr[x+1][y] != 1 and arr[x][y+1] !=1 and arr[x+1][y+1] != 1:
                dfs('a', [x+1, y+1])

dfs('r', [0, 1])

print(cnt)

#끝까지 탐색해야하는 점에서 dfs 풀이를 생각했다.
#dfs라고 무조건 스택에 쌓아야 하는 것은 아니다. 무지성으로 stack에 append하고 pop 안해도 된다.
#문제에서 꼭 필요한 상황에서 사용해야 한다.
#이 문제에선 조건들을 체크해서 재귀로 돌리고 최종 도달하는 지점에만 카운트를 세주면 된다.

#global 설정하는 것
#경계값을 잘 보자(x+1<n, y+1<n) 은근 헷갈린다. 인덱싱 에러.