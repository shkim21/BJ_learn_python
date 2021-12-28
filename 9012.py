import sys

T = int(sys.stdin.readline())

def check_VPS(s):
    stack = []
    for i in range(len(s)):
        if i == 0:
            stack.append(s[i])
        else:
            #리스트가 비어있을 때 인덱싱 에러
            if len(stack) > 0:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        # print("stack:", stack)
    
    if stack == []:
        print("YES")
    else:
        print("NO")

for _ in range(T):
    s = sys.stdin.readline().strip()
    check_VPS(s)
