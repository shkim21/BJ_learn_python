T = int(input())

for i in range(T):
    N = int(input())
    Dic = {}
    L_list = []
    for j in range(N):
        S, L = map(str, input().split())
        L = int(L)
        Dic[L] = S
        L_list.append(L)
    p = max(L_list)
    print(Dic.get(p))