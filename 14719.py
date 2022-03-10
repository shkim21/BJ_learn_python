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