N, M = map(int, input().split())

visited = [False]*(N+1)
s = [] #저장하는 
history = []

def dfs():
    #if #길이가 M이면 리턴
    if len(s) == M: #이미 했던 것 없으면 중복제거
        sorted_s = sorted(s)
        # print("history:", history)
        if sorted_s not in history:
            history.append(sorted_s)
            print(*sorted_s) #print(' '.join(map(str, s)))
        return s
    
    for i in range(1, N+1):
        if not visited[i]: 
            visited[i] = True
            s.append(i)

            dfs()

            visited[i] = False
            s.pop()
    return s

dfs()

#다른 풀이 start 변수추가
N, M = map(int, input().split()) 
lst = [] 

def dfs2(start): 
    if len(lst) == M: # 탈출 조건 
        print(' '.join(map(str, lst))) 
        return #아무것도 리턴 안해줘도 상관없음. 함수만 종료시키면!
        
    for i in range(start, N+1): 
        if i not in lst: 
            lst.append(i) 
            dfs2(i+1) 
            lst.pop() 
            
            
dfs2(1)
