n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0] * (m+1) for _ in range(n+1)]#곡개수 n개, 최대 볼륨값을 길이로 갖는 배열
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j+v[i] <= m:
                dp[i+1][j+v[i]] = 1
            if j-v[i] >= 0:
                dp[i+1][j-v[i]] = 1

ans = -1#디폴트 값 설정하고
for i in range(m, -1, -1):#뒤에서 부터 돔
    if dp[n][i]==1:
        ans = i#인덱스로 찾음
        break
print(ans)
