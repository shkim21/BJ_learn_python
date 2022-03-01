N = int(input())
Nlist = list(map(int, input().split()))
Nlist.sort()
M = int(input())
Mlist = list(map(int, input().split()))

ans = []

# def find(m, Nlist):
#     # print("m:", m)
#     # print("Nlist:", Nlist)
#     l = len(Nlist)
#     if l == 1:
#         if int(m) == int(Nlist[0]):
#             return 1
#         else:

#             return 0
#     else:
#         if m >= Nlist[l//2]:#2
#             return find(m, Nlist[l//2:])
#         else:
#             return find(m, Nlist[:l//2])

def binarySearch(element, some_list, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if element == some_list[mid]:
        return 1
    elif element > some_list[mid]:
        start = mid + 1
        return binarySearch(element, some_list, start, end)
    elif element < some_list[mid]:
        end = mid -1
        return binarySearch(element, some_list, start, end)
    

for i in Mlist:#0, 1, 2,
    # a = find(i, Nlist)
    a = binarySearch(i, Nlist, 0, len(Nlist)-1)
    # print("a:", a)
    ans.append(str(a))

# print("ans:", ans)
print(' '.join(ans))