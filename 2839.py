N = int(input())

y = N // 5

ans = []
# print("y", y)
for i in range(y+1):
    a = N - (5*i)
    # print("a:", a)
    if (a % 3) == 0:
        # print("a//3+i:", a//3+i)
        ans.append(a//3+i)
    
if ans:
    print(min(ans))
else:
    print("-1")