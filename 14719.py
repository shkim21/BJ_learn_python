h, w = map(int, input().split())
w_list = list(map(int, input().split()))

r_max = w_list[0]
l_max = w_list[-1]
rm_list = []
lm_list = []

for i in w_list:
    r_max = max(r_max, i)
    rm_list.append(r_max)

for j in range(w-1, -1, -1):#0, 1, 2  (w-1, -1, -1)
    # print("j:",j)
    l_max = max(l_max, w_list[j])
    lm_list.insert(0, l_max)

# print("rm_list:", rm_list)
# print("lm_list:", lm_list)

rs = []
for k in range(w):
    rs.append(min(rm_list[k], lm_list[k]) - w_list[k])

# print("rs:", rs)
print(sum(rs))

###더 간결한 풀이
h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):#포문 하나로 비교!
    left_max = max(world[:i])#리스트 인덱싱 해서
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:#작을 경우에만 계산!
        ans += compare - world[i]

print(ans)