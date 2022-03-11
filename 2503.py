from itertools import permutations#중복 순열,

n = int(input())

num = [i for i in range(1, 10)]
print(num)

for _ in range(n):
    nums, s, b = map(int, input().split())
    nums = str(nums)
    first = int(nums[0])
    second = int(nums[1])
    third = int(nums[2])


#문제를 잘못 이해했나,,, 모든 경우를 세는 줄 알았음
#각각의 스트라이크, 볼의 경우에 따라서 가능한 모든 경우를 세고

#브루트 포스로 재도전 해볼것!