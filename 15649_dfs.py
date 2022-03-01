N, M = map(int, input().split())
s = []
visited = [False]*(N+1)

def DFS():
    if len(s) == M:#종료조건!
        print("s:", s)
        print(*s)## printing the list using * operator separated by space 
        return
    
    for i in range(1, N+1):
        if visited[i]:#이미 방문했으면 패스
            continue

        visited[i] = True#방문체크
        s.append(i)#출력 리스트에 넣음
        
        DFS()#함수 다시 호출

        s.pop()#원상복귀 과정 필요
        visited[i] = False

DFS()
