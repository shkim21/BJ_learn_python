h, m, s = map(int, input().split())
t = int(input())

t_h = t//3600
t_m = t//60
while t_m > 59:
    t_m = t_m % 60 

t_s = t - t_m*60 - t_h*3600

h = h + t_h
m = m + t_m
s = s + t_s

while s > 59:
    s = s - 60
    m = m + 1
while m > 59:
    m = m - 60
    h = h + 1
while h > 23:
    h = h - 24

print(h, m, s)