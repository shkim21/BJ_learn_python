import sys
from collections import deque

N = int(input())

deq = deque()

for _ in range(N):
    inputs = list(sys.stdin.readline().split())
    # print("inputs:", inputs)
    string = inputs[0]
    # print("string", string)

    # print("deq:", deq)

    if string == "push":
        deq.append(int(inputs[1]))

    if string == "pop":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())

    if string == "size":
        print(len(deq))

    if string == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    if string == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    if string == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq)-1])

    # print("deq2:", deq)