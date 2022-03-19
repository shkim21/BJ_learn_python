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

#완전탐색이 여기서 충분히 실현가능할지 시간복잡도 계산 해야 했음.
#입력이 작은 경우, 연산이 크지 않은 경우
#최대 입력에 대해서 최대 연산이 계산 가능한 정도