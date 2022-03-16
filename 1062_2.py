from itertools import combinations

n, k = map(int, input().split())

known = ['a', 'c', 'i', 'n', 't']
learn = set()
words = []

for _ in range(n):
    ss = input()
    tmp = set()
    for s in ss[4:-4]:
        if s not in known:
            learn.add(s)
            tmp.add(s)
    words.append(list(tmp))

# print('learn:', learn)#조합을 위한 안 배운 글자들
# print("words:",words)#중복 제거한 배우지 않은 글자

if k < 5:
    print(0)
else:
    k -= 5
    mx = 0

    if k > n:#조합하는 과정에서 문제 해결
        k = n

    for com in combinations(list(learn), k):
        items = set(list(com))
        # print("items:", items)
        tm = 0
        for word in words:
            if set(word).issubset(items):
                # print("items:", items)
                # print("word:",word)
                tm += 1
        mx = max(mx, tm)
    print(mx)


#set으로 풀었는데 51%에서 틀림.. 왜 틀린지 모르겠음.
#비트마스킹 풀이