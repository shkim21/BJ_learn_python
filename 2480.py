a, b, c = map(int, input().split())

d_list = []
d_list.append(a)
d_list.append(b)
d_list.append(c)

d_set = set()
d_set.update(d_list)

if len(d_set) == 1:
    to_list = list(d_set)
    p = to_list[0]
    print(10000+p*1000)

elif len(d_set) == 3:
    to_list = list(d_set)
    p = to_list[2]
    print(p*100)

elif len(d_set) == 2:
    d_list.sort()
    if d_list[0] == d_list[1]:
        p = d_list[0]
        print(1000+p*100)
    else:
        p = d_list[1]
        print(1000+p*100)