x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = []
x.append(x1)
x.append(x2)
x.append(x3)
x.sort()

y = []
y.append(y1)
y.append(y2)
y.append(y3)
y.sort()

if x[0] == x[1]:
    x4 = x[2]
else :
    x4 = x[0]

if y[0] == y[1]:
    y4 = y[2]
else :
    y4 = y[0]

print(x4, y4)