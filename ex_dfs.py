graph = {
	1: [2,3,4],
	2: [5],
	3: [5],
	4: [],
	5: [6,7],
	6: [],
	7: [3],
}


#스택 이용한 반복 구조로 구현
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]#스택에 넣음

    print("stack:", stack)

    while stack:
        v = stack.pop()#스택에서 제일 마지막으로 구현된 것을 빼고 리턴
        print("v:", v)
        if v not in discovered:#발견되지 않았을 때
            print("discovered v:", discovered, v)
            discovered.append(v)
            print("graph[v]:", graph[v])
            for w in graph[v]:#인접간선 추출
                print("w:", w)
                stack.append(w)
	
    return discovered

#스택에 인접 노드 쌓아서 저장후 맨 뒤에서부터 하나씩 빼내서 돌림
print(iterative_dfs(1))