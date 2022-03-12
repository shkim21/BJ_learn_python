n, s = map(int, input().split())

n_list = list(map(int, input().split()))

dp = []
ans = 0

if n_list[0]>= s:
    dp.append(1)

for i in range(n):
    # print("i:",i)
    for j in range(i-1, -1, -1):
        # print("j:",j)
        hap = sum(n_list[j:i+1])
        # print("hap:",hap)
        if hap >= s:
            dp.append(i-j+1)
            break

# print("dp:",dp)
print(min(dp))

#시간초과난 풀이