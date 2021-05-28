N = int(input())

class Stack:
    #s =[]

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
    a = input()

    if len(a.split()) == 2:
        s.push(a[5:])

    elif a == "pop":
        print(s.pop())

    elif a == "size":
        print(s.size())

    elif a == "empty":
        print(s.is_empty())

    elif a == "top":
        print(s.top())