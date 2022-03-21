from collections import deque

s = int(input())

dp = [0]*(1001)
dp[1] = 0

def bfs():
    queue = deque()
    queue.append(1)

    while queue:
        v = queue.popleft()

        if v == s:
            print(dp[v])
            break
        

stack = []
clip = 0
win = 1
cnt = 0

def dfs(start):
    global win, clip, cnt
    stack.append(start)

    if stack:
        
        #클립보드에 있는 숫자 더하고
        win += clip
        
        if win == s:
            return
        #클립보드 업데이트
        clip = win

        cnt += 1
        #1 빼기


#dfs를 생각한 이유 : 각각의 경우에 대해서 브루트 포스를 해야한다고 생각함,,