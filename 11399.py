import sys
input = sys.stdin.readline
N = int(input())

num_list = list(map(int, input().split()))
num_list.sort()
# print(num_list)
sum = 0
for i in range(N):
    sum += num_list[i]*(N-i)

print(sum)

#easy 한 문제. 11분컷
#입력 받는 것과 공백 포함한 입력값 잘라서 int 맵핑 후 리스트에 넣기