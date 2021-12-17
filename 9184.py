#이문제의 핵심 : 적당한 크기의 배열을 선언(3차원, 20)&초기화해서 집어넣기. 값이 존재한다면 바로 리턴시키기

run = True

# arrays = [[[0]*21]*21]*21 #틀림!! 왜...??
arrays = [[[0]*(21) for _ in range(21)] for _ in range(21)]#초기화 (최대 20까지임)
#배열 만드는 것!! 제대로 만들 것

def w(a, b, c):
    # print("a b c:", a, b, c)
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if arrays[a][b][c]: #존재할 때 바로 리턴해주는 것!! 시간 단축 핵심!!
        return arrays[a][b][c] 
    if a < b < c:
        arrays[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return arrays[a][b][c]

    arrays[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return arrays[a][b][c]

while(run):
    a, b, c = map(int, input().split())

    if a==-1 and b==-1 and c==-1:
        run = False
        break

    ans = w(a, b, c)

    print("w({}, {}, {}) = {}".format(a, b, c, ans))
