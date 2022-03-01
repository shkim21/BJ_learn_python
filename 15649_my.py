N, M = map(int, input().split())

visited = [0]*(N+1)
stack  = []

def dfs():
    #종료 조건 프린트
    if len(stack)==M:
        print(*stack)
        return
    
    for i in range(1, N+1):#1,2,3,,,N
        #방문했으면 패스
        if visited[i] == True:
            continue

        stack.append(i)
        visited[i] = True
        dfs()
        stack.pop()
        visited[i]= False

dfs()