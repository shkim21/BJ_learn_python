
from itertools import permutations

# ex = ['a', 'a', 'b', 'c', 'd']
# p = list(permutations(ex, 5))
# print(len(p))

# for idx, p in enumerate(ex):
#     print('idx:', idx)
#     print('p:', p)



n = int(input())

a_list = list(map(int, input().split()))

plus, minus, multi, div = map(int, input().split())
results = []
yeonsan = []

for _ in range(plus):
    yeonsan.append('p')
for _ in range(minus):
    yeonsan.append('m')
for _ in range(multi):
    yeonsan.append('mu')
for _ in range(div):
    yeonsan.append('d')

# print(yeonsan)

# def plus(a, b):
#     return a + b

# def minus(a, b):
#     return a - b

# def multiple(a, b):
#     return a * b

def divide(a, b):
    if a < 0:
        return -((-a) // b)
    else:
        return a // b

# print("div:",divide(-1, 3))

permutas = list((permutations(yeonsan, len(yeonsan))))
# print("permutas:", permutas)


for pm in permutas:#pm : ('d', 'c', 'b', 'a', 'a')
    tmp = a_list[0]
    # print("pm:", pm)
    for idx, y in enumerate(pm):#'p'
        #idx: 0, 1, 2, ,,
        # print("idx:", idx)
        # print("y:",y)
        if idx == len(pm):
            # print("end!")
            break
        if y == 'p':
            tmp += a_list[idx+1]
        elif y == 'm':
            tmp -=a_list[idx+1]
        elif y == 'mu':
            tmp *= a_list[idx+1]
        else:
            tmp = divide(tmp, a_list[idx+1])
    # print("tmp:", tmp)
    results.append(tmp)

# print("results:", results)

print(max(results), min(results))



