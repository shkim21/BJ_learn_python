def solve(a: list) -> int:
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

b = [1, 2, 3, 4, 5, 6]

print(solve(b))