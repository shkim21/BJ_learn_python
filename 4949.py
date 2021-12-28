import sys

def check_VPS(s):
    stack = []
    for i in range(len(s)):
        # print("s[i]:", s[i])
        if i == 0:
            stack.append(s[i])
        else:
            if len(stack) > 0:
                if '(' == stack[-1] and s[i] == ')':
                    stack.pop()
                elif '[' == stack[-1] and s[i] == ']':#조건문 여러개. 위에 if 돌고 다음 if else 연결됨
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        # print("stack:", stack)
    
    if stack == []:
        print("yes")
    else:
        print("no")

def check_VPS2(s):
    ex = []
    target = ['(', ')', '[', ']']
    for i in range(len(s)):
        if s[i] in target:
            ex.append(s[i])
    check_VPS(ex)

while(1):
    inputs = sys.stdin.readline().strip('\n')
    # print("inputs:", inputs)
    if inputs == '.':
        break
    check_VPS2(inputs)


#에러 원인 if '(' in stack 으로 하면 안되고 stack의 마지막이 짝이 맞아야 한다.
#테케 다 통과해서 맞은 줄 알았지만 채점에서 어림도 없지