import math

words = str(input())
l = len(words)
n = math.trunc(len(words)/2)
p = 0
for i in range(n):
    if words[i] != words[l-1-i]:
        p += 1

if p != 0:
    print(0)
else:
    print(1)