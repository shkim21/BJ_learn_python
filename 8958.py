T = int(input())

count = []

for _ in range(T):
    words = list(input())
    N = len(words)
    #print(N)
    count = [0]*N
    #print(count)
    for i in range(N):
        if words[i] == 'O':
            count[i] = 1
        for j in range(1, N):
            if words[j] == words[j-1] and words[j] == 'O':
                count[j] = int(count[j-1]) + 1        
    #print(count)
    M = len(count)
    p = 0
    for i in range(M):
        p += count[i]

    print(p)