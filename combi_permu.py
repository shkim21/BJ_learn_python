from itertools import permutations
from itertools import combinations

a = []
b = []
items= [1,2,3,4]

#조합
for i in list(combinations(items,2)):
    a.append(i)
print(a)

#순열
for i in list(permutations(items,2)):
    b.append(i)
print(b)


def comb(lst, n):
    ret = [] #빈리스트

    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)-n+1):
            print("i:", i)
            print("lst[i+1:]:", lst[i+1:])
            for temp in comb(lst[i+1:], n-1):
                print("temp:", temp)
                ret.append([lst[i]]+temp)
    return ret
print("comb:", comb([1,2,3,4],2))