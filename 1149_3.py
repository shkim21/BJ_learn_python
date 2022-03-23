n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

d = [[0 for _ in range(3)] for _ in range(n)]

d[0][0] = arr[0][0]
d[0][1] = arr[0][1]
d[0][2] = arr[0][2]

for i in range(1, n):
    d[i][0] += min(d[i-1][1], d[i-1][2]) + arr[i][0]
    d[i][1] += min(d[i-1][0], d[i-1][2]) + arr[i][1]
    d[i][2] += min(d[i-1][0], d[i-1][1]) + arr[i][2]

# print("d:",d)
print(min(d[n-1]))