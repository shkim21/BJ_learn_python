from collections import deque

N = int(input())

cards = [i for i in range(1, N+1)]

# print(cards)
deq = deque(cards)

while(1):
    if len(deq) == 1:
        print(deq[0])
        break
    else:
        deq.popleft()
        deq.rotate(-1)