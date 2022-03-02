N, M = map(int, input().split())

s = []

def dfs():
    if len(s) == M:
        print(*s)
        return
    
    for i in range(1, N+1):
        
        if len(s)> 0:
            if s[-1] <= i:
                s.append(i)
                dfs()
                s.pop()
        else:
            s.append(i)
            dfs()
            s.pop()
    return

dfs()