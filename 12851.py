from collections import deque

n, k = map(int, input().split())
cnts = [[-1, 0] for _ in range(100001)]#[0]*(100001)#각 인덱스 위치에 얼마만에 올 수 있는지, 첫번째 인덱스: 최소방법, 두번째 인덱스: 방법수

def bfs(start):

    queue = deque()
    queue.append(start)
    cnts[start][0] = 0# 0번째
    cnts[start][1] = 1#초기값 셋팅 방법 1

    while queue:
        v = queue.popleft()
        
        moves = [v-1, v+1, v*2]
        for m in moves:
            if 0<=m<=100000:
                if cnts[m][0] == -1:# 0일때만? (0 아닐 때는 패쓰. 더 적은 수로도 갈 수 있다는 거니깐.)
                    cnts[m][0] = cnts[v][0] +1
                    cnts[m][1] = cnts[v][1]
                    queue.append(m)

                elif cnts[m][0] == cnts[v][0]+1:#0 아닐 때, 즉 이전에 방문했더라도 최소로 방문할 수 있다면 (이 경우 생각해내는 것이 이 문제의 핵심!)
                    cnts[m][1] += cnts[v][1]
                    #경우의 수를 업데이트 해줘야함


                
bfs(n)

# print("cnt:", cnts[:200])
print(cnts[k][0])
print(cnts[k][1])


#핵심! 이전엔 최단거리가 아니었더라도 최단거리가 될 수 있는 경우가 있다! 그부분을 체크해줘야 함!