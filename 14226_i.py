from collections import deque

#(s:화면에 출력된 이모티콘 갯수, c:클립보드에 있는 이모티콘 갯수)

n = int(input())
emoji = [[-1 for _ in range(n+1)] for _ in range(n+1)] #2차원 배열
print("emoji:", emoji)

def bfs(n):
    queue = deque()
    queue.append((1, 0))
    emoji[1][0] = 0 #화면에 하나, 클립보드에 아무것도 없음

    while queue:
        s, c = queue.popleft()
        print("s:", s, "c:", c)
        #-1이랑 비교하는 이유가, 연산을 안한 것을 이렇게 체크함!
        if emoji[s][s] == -1:#방문하지 않았을 때
            emoji[s][s] = emoji[s][c] + 1 #클립보드에 모두 복사함
            queue.append((s,c))
        if s+c <= n and emoji[s+c][c] == -1:
            emoji[s+c][c] = emoji[s-1][c] + 1#이모티콘을 화면에 붙임
            queue.append((s+c, c))
        if s-1 >= 0 and emoji[s-1][c] == -1:
            emoji[s-1][c] = emoji[s][c] + 1#이모티콘 하나 삭제   #숫자 1씩 증가시킴
            queue.append((s-1, c))


bfs(n)

ans = -1
for i in range(n+1):
    if emoji[n][i] != -1:#-1이 아닐때
        if ans == -1 or ans > emoji[n][i]:#처음 경우 고려, 
            ans = emoji[n][i]#업데이트

#두번째 방법 값 업데이트 방식 차이
r = emoji[n][1]
for i in range(1, n):
    if emoji[n][i] != -1:
        r = min(r, emoji[n][i])

#DP, BFS 혼합 문제
#최단시간 : BFS,,

#2가지를 고려해야할 때 2차원 배열을 써라!

#cnt를 2개의 변수로 이루어진 2차원 배열의 값으로 집어 넣음
#배열의 인덱스로 접근하는 아이디어 [s+c][s]