from collections import deque

N, K = map(int, input().split())

people = [i for i in range(1, N+1)]

deq = deque(people)

ans = []



for i in range(N):
    deq.rotate(-(K-1))
    ans.append(deq.popleft())
    # print("ans:", ans)

print("<", end="")
print(str(ans)[1:-1], end="")
print(">")