N = int(input())
y = N // 5
ans = []
for i in range(y+1):
    a = N - (5*i)
    if (a % 3) == 0:
        ans.append(a//3+i)
    
if ans:
    print(min(ans))
else:
    print("-1")