N, K = map(int, input().split())

A_list = []

for i in range(N):
    element =  int(input())
    A_list.append(element)

ans = 0

for i in range(N): # N : 10, i : 0, 1, 2, 3,,
    iter = N - i - 1
    #print("iter:", iter)
    ahrt = K // A_list[iter]
    if ahrt == 0:
        continue
    elif K // ahrt: #몫이 있는 경우
        #print("ahrt:", ahrt)
        ans += ahrt
        K = K - (ahrt)*A_list[iter]
        #print("K:", K)
    else:
        continue

#print("A_list:",A_list)

print(ans)