import sys

N = int(sys.stdin.readline())
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.stack.pop()

    def size(self):#아무것도 들어가지 않아도 self 선언 필요! 클래스 내부 메서드 구현 기본기 다시 확실히 알아볼 것!
        return len(self.stack)

    def is_empty(self):
        if self.stack == []:
            return 1
        else:
            return 0

    def top(self):
        if self.is_empty():
            return -1
        else:
            return self.stack[-1]

s = Stack()

for _ in range(N):
    a = sys.stdin.readline()
    b = a.split()

    if len(b) == 2:
        s.push(a[5:].strip('\n')) #sys.stdin.readline()으로 받으면 뒤에 \n까지 입력 받게 된다!

    elif b[0] == "pop":
        print(s.pop())

    elif b[0] == "size":
        print(s.size())

    elif b[0] == "empty":
        print(s.is_empty())

    elif b[0] == "top":
        print(s.top())

#입력 받는 것 input() -> sys.stdin.readline()으로 바꾸니깐 시간초과 해결됨,,,!
#stack in python : list
#push : append
#pop : pop() 제일 마지막에 들어간 것 제거 + 반환
