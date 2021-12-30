from collections import deque

deq = deque()

deq.appendleft(10)

deq.append(0)

#
deq.popleft()

deq.pop()

arr = [1, 2, 3]
deq.extend(arr)

deq.extendleft(arr)

deq.rotate(2)#num 만큼 회전 양수면 오른쪽, 음수면 왼쪽

###ex

a = [1, 2, 3, 4, 5]

q = deque(a)
q.rotate(2)
result = list(q)
print("result:", result)    