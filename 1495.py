n, s, m = map(int, input().split())
vlms = list(map(int, input().split()))
dp = [0]*(m+1)
dp[s] = 1

t = True

for i in range(n):
    if t:
        idxs = []
        for j in range(m+1):
            if dp[j]:
                idxs.append(j)

        for k in idxs:
            up = k + vlms[i]
            down = k - vlms[i]
            dp[k] = 0#초기화
            if 0<=up<=m or 0<=down<=m:
                if 0<=up<=m:
                    dp[up] = 1
                if 0<=down<=m:
                    dp[down] = 1
            else:
                continue
        #dp가 전부 0일때
        no = 0
        for l in range(m+1):
            if dp[l]:
                no =1
        if not no:
            print(-1)
            t = False
            break


if t:
    max_idx = 0
    for i in range(m+1):
        if dp[i]:
            max_idx = max(max_idx, i)
    print(max_idx)


##반례도 다 통과하는데 왜 틀린지 모르겠음...