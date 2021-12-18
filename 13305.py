N = int(input())

road_l = list(map(int, input().split()))
liter_price = list(map(int, input().split()))

total_price = 0

for i in range(N-1):
    a = min(liter_price[:i+1]) * road_l[i]
    total_price += a

print(total_price)

#초기 생각 : 리스트에서 최소값 구해서 거리에 곱해주기
