N = int(input())
count = 0
if N < 100:
    count = N
    print(count)
else:
    for n in range(100, N+1):
        first = n // 100
        second = (n - first*100) // 10
        third = n % 10
        if (first - second) == (second - third):
            count += 1
    
    print(count + 99)