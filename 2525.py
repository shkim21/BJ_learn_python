h, m = map(int, input().split())
p = int(input())

m = p + m

while m > 59:
    m = m - 60
    h = h + 1
    if h > 23:
        h = h - 24
    
print(h, m)