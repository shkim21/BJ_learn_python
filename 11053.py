N = int(input())

Alist = list(map(int, input().split()))

# print("Alist:", Alist)

s = []

for start in range(N):#0, 1, 2,,,N-1
    temp = []
    temp.append(Alist[start])
    # print("temp before:", temp)
    # print("start:", start)
    for inner in range(0, start):
        # print("inner:", inner)
        if temp[-1] > Alist[inner]:
            temp.insert(0, Alist[inner])
            # print("temp insert:", temp)
    # print("temp after:", temp)
    s.append(len(temp))

# print("s:", s)
# print(max(s))


#DP,,
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if Alist[i] > Alist[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))