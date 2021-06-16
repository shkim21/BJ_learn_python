N, X = map(int, input().split())

x = []

x.append(input().split())

y = []
for i in range(N):
    if int(x[0][i]) < X:
        y.append(int(x[0][i]))

for j in range(len(y)):
    print(y[j], end=' ')