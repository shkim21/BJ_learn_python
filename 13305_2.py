N = int(input())

road_l = list(map(int, input().split()))
liter_price = list(map(int, input().split()))

total_price = 0
min_price = liter_price[0]

for i in range(N-1):
    if min_price > liter_price[i]:
        min_price = liter_price[i]
    # a = min(liter_price[:i+1]) * road_l[i]
    total_price += min_price * road_l[i]

print(total_price)

#초기 생각 : 리스트에서 최소값 구해서 거리에 곱해주기
