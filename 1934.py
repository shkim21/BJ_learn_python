T = int(input())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

for _ in range(T):
    a, b = map(int, input().split())
    c = a * b // gcd(a, b)
    print(c)
