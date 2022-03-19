# n, k = map(int, input().split())

# s = []#개수 담는 리스트
# stack = []
# cnt = 0

# def dfs(p, cnt):
    # # stack.append(p)

    # if p == k:
    #     print("in!")
    #     return
    # else:
    #     cnt += 1
    #     stack.extend([p+1, p-1, p*2])
    #     print("stack:", stack)
    #     stack.pop(0)
    #     for i in stack:#10, 6, 4
    #         dfs(i, cnt)
    #         stack.pop(0)
    # if k in stack:
    #     print("end stack:", stack)
    #     return
    
    # for i in stack:
    #     stack.extend([i+1, i-1, i*2])
    #     print("stack:", stack)

# stack.append(n)
# print("result:", dfs(n, cnt))

from collections import deque

n, k = map(int, input().split())

cnts = [0]*(100000+1)#인덱스 번호가 그 수로 가기 위한 최소의 연산

def bfs(a):
    queue = deque()
    queue.append(a)

    while queue:
        # print("queue:", queue)
        v = queue.popleft()
        if v ==k:
            print(cnts[v])
            break
        # print("v:", v)
        moves = [v+1, v-1, v*2]
        for m in moves:
            # if m == k:
            #     print(cnts[v])
            #     return cnts[v]
            # else:
            # print("m:", m)
            if 0<=m<=100000 and not cnts[m]:#in 써서 시간초과? 와,,, if문 조건 순서도 중요한듯,,, 인덱스 에러 뜸.  not cnts[m] 하는 이유가 0이 아니면 패쓰함. 왜나하면 더 이전 값이 있으니깐.
                cnts[m] = cnts[v]+1
                # print("cnts[m]:", cnts[m])
                queue.append(m)#와 순서도 중요하구나,,,!! append 먼저 시키면 뒤에 줄이 실행이 안됨! 바로 while queue 실행됨
    # return 

bfs(n)

# print("cnts:", cnts)