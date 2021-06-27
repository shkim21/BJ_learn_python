N = int(input())
x_list = []
y_list = []
for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

c = []

for i in range(len(x_list)):
    d = 0
    for j in range(len(x_list)):
        if x_list[i] < x_list[j] and y_list[i] < y_list[j]:
            d += 1
    d += 1
    c.append(d)

print(*c, sep=' ')