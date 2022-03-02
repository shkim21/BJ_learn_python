N, M = map(int, input().split())
#Q방문여부 체크 불필요!
s = []

def dfs():
    if len(s) == M:
        print(*s)
        return

    for i in range(1, N+1):
        s.append(i)

        dfs()
        s.pop()
    return s

dfs()