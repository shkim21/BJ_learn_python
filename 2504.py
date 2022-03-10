import sys

input = sys.stdin.readline
strings = input().strip()
stack = []
# stack.extend(strings.strip())
# print(stack)
# stack.append(strings[0])

def is_empty(stk):
    if len(stk) == 0:
        return True
    else:
        return False

tmp = []
num = 1

for s in strings:
    print("s:",s)
    print("stack:", stack)
    if s == ')' and stack[-1] == '(':
        stack.pop()
        num *= 2
        if is_empty(stack):
            tmp.append(num)
            num = 1#초기화
        
        continue#not append at stack
    if s == ']' and stack[-1] == '[':
        stack.pop()
        num *= 3
        if is_empty(stack):
            tmp.append(num)
            num = 1
        continue
    stack.append(s)

print("stack", stack)
print("tmp:", tmp)
if stack == []:
    print("empty")
else:
    print("0")


#괄호 닫을 때 임시 값 설정하는건 좋앗으나, 여러개를 처리(x+y) 하는 부분에서 막힘
#stack 이용하는 방향은 맞았으나, 임시값을 다시 나눠주는(?) 것을 생각하지 못함