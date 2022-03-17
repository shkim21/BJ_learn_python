import heapq

n, k = map(int, input().split())
ordered = list(map(int, input().split()))
# print("orderd:", ordered)

hq = []
cnt = 0

for o in ordered:
    # print("o:", o)
    # print("hq:", hq)
    ### heapq._heapify_max(hq)
    if (-o, o) not in hq:#중복체크
        if len(hq) == n:#
            v = heapq.heappop(hq)[1]#큰 값 pop
            # print("v:", v)
            cnt += 1
        
        heapq.heappush(hq, (-o, o))
    else:
        pass

print(cnt)

#문제 이해 미스,,,
#우선순위에 따른 pop이면 최소가 되는 줄 암..
#아니 근데 문제 설명이 불충분한거 아이가,,, 나중에 쓰면 우선순위가 올라가는 걸 말해줘야 하는 거 아님?!