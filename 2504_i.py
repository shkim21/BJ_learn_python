s = input()
stack = []
tmp = 1#임시 값
res = 0 #최종 값

#스택에 쌓는 것에서 효율적으로 접근하면 안되고 하나하나 돌아야 함. 조건이 많음.
# for c in s를 하면 안 되고 길이로 돌아야 함!! 인덱스로 접근
for i in range(len(s)):#i: 0, 1, 2,,,
    print("tmp:", tmp)
    print("res:", res)
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])

    elif s[i] == ')':
        if not stack or stack[-1] == '[':#종료조건(비어있을 때 or 다른 괄호 여는 거 - 무조건 올바르지 않음)
            res = 0
            break
        if s[i-1] == '(':
            res += tmp
        tmp //= 2 #tmp 값을 계속 유지하고 가지고 가야함. 괄호를 없애고(pop) 이전값으로 돌아가야 함. 임시값을 저장하고 있어야함!
        stack.pop() # pop도 까먹지 말고 꼭
    
    else:# ]
        if not stack or stack[-1] == '(':
            res = 0
            break
        # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
        # 단, 이 경우는 오류는 아님
        if s[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop() # pop 까먹지 말기

if stack:#비어 있지 않았을 때
    res = 0
print(res)

#이 문제의 핵심 : 문제의 종료조건, 임시값을 가지고 가야 하는 것. 연산을 하고 다시 되돌려 놓는 것(/2, /3)
#괄호가 시작될 때 곱하기 연산을 하는 것. 괄호가 닫힐 때는 이때까지 저장된 값 이용해서 연산하기