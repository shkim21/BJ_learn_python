N = int(input())
T = True
M = N
count = 0

while T:
    first = 0
    second = 0
    next = 0
    
    first = M // 10
    second = M % 10
    next = (first + second) % 10

    M = second * 10 + next
    count += 1

    if M == N:
        print(count)
        T = False
        break