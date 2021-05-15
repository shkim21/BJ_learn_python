T = int(input())
s = []
for i in range(1, T+1):
    a, b = map(int, input().split())
    s.append(a + b)
    
for i in range(0, T):
    print("Case #{0}:".format(i+1), s[i])