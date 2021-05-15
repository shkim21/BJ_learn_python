T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c = a + b
    print("Case #{0}: {a} + {b} = {c}".format(i+1, a=a, b=b, c=c))