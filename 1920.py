N = int(input())
N_list = map(int, input().split())
M = int(input())
M_list = map(int, input().split())

N_sort = sorted(N_list)
# print("N_sort:", N_sort)

def bn_search(element, lst, start=0, end=N-1):#end 범위 조심!
    if start > end:
        return 0
    mid = (start+end) // 2
    # print("mid:", mid)
    if element == lst[mid]:
        return 1
    elif element > lst[mid]:
        start = mid +1
        return bn_search(element, lst, start, end)
    elif element < lst[mid]:
        end = mid -1
        return bn_search(element, lst, start, end)

for m in M_list:
    print(bn_search(m, N_sort))