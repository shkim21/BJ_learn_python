# def dfs_perm(lst,n):
#     ret = []
#     idx = [i for i in range(len(lst))]#리스트 길이별 인덱스 저장
#     print("idx:", idx)

#     stack  = []
#     for i in idx:
#         stack.append([i])

#     print("stack:", stack)

#     while len(stack)!=0:
#         cur = stack.pop()#스택 마지막 원소 리턴
#         print("cur:", cur)

#         for i in idx:#0, 1, 2, 3
#             print("i:", i)
#             if i not in cur: #cur에 없을 때
#                 temp = cur+[i] #마지막 원소 + i
#                 print("temp:", temp)
#                 print("n:", n)
#                 if len(temp)==n:
#                     element = []
#                     for i in temp:
#                         element.append(lst[i])
#                     print("element:", element)
#                     ret.append(element)
#                 else:
#                     stack.append(temp)
#         print("ret:", ret)
#         print("stack2:", stack)


# dfs_perm([1, 2, 3, 4], 2)

l = [1, 2, 3, 4]
visited = [0 for _ in range(len(l))]#방문했던 곳 저장하는
print("visited:", visited)
answer = []

def dfs(cnt, list):
    print("cnt:", cnt)
    print("list1:", list)
    if cnt == len(l):
        answer.append(list[:])
        print("answer:", answer)
        return

    for i, val in enumerate(l):
        print("i:", i, ", val:", val)
        # 만약 방문했다면 건너 뛰기(순열을 위함)
        if visited[i] == 1:
            print("continue")
            continue

        # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)
        visited[i] = 1
        print("list2:", list)
        print("visted:", visited)

        dfs(cnt+1, list)
        # 방금 전 list에 추가한 값과 방문 한 것을 되돌려주기
        list.pop()
        print("list3:", list)
        visited[i] = 0
        print("visited 3:", visited)


dfs(0, [])
print(answer)