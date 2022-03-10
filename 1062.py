n, k = map(int, input().split())


def dfs(lst, leng):
    
    if leng == 0:
        return
    



if k < 5:
    print("0")
else:
    basic = {'a', 'c', 'i', 'n', 't'}
    ex = []
    for _ in range(n):
        inputs = input()
        tmp = set()
        for i in inputs:#한 글자씩
            if i not in basic:
                tmp.add(i)

        print("tmp:", tmp)
        if len(tmp) > k -5:
            continue
        ex.append(list(tmp))
    print("ex:", ex)

#dfs 풀이 구상하다가 막혔음.. 무엇을 인자로 줄지, 어떻게 반복을 시킬지, 종료는 어떻게 할지 생각하다가 머리 터짐...ㅠ


