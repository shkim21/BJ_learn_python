def d(n): #n과 n의 각 자리수를 더하는 함수 n : 최대 4자리수
    s= []
    for i in range(1, n+1):
        fourth = i // 1000
        third = (i - fourth*1000) // 100
        second = (i - fourth*1000 - third*100) // 10
        first = i % 10

        s.append(i + fourth + third + second + first)

    s.sort()

    a = list(range(1, n+1))
    z = list(set(a) - set(s))
    z.sort()
    for i in z:
        print(i)

d(10000)
