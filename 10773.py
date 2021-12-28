import sys

K = int(sys.stdin.readline())
nums = []
for _ in range(K):
    a = int(sys.stdin.readline())
    if a == 0:
        nums.pop()
    else:
        nums.append(a)

    # print("nums:", nums)

print(sum(nums))