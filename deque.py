#deque : double-ended queue
#양방향에서 데이터 처리

import collections


#append(x) : 오른쪽에 추가
deq = collections.deque(['a', 'b', 'c'])
deq.append('d')
print(deq)

#appendleft(x) : 왼쪽에 추가
deq.appendleft('e')

#extend(iterable) 
deq.extend('fg')
print(deq)
#f, g

#extendleft(iterable)
deq2 = collections.deque(['a', 'b', 'c'])
deq.extendleft('de')
print(deq)
#deque(['e', 'd', 'a', 'b', 'c'])

#pop() : 오른쪽에서 부터 차례대로 제거&반환
deq2.pop()

#popleft()
deq2.popleft()

#rotate(n) : 값만큼 회전. 음수면 왼쪽으로 회전, 양수면 오른쪽으로 회전
deq3 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq3.rotate(1) # e a b c d

deq3.rotate(-1)



