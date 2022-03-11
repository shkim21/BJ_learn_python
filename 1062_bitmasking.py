from itertools import combinations

n, k = map(int, input().split())

if k < 5:
    print(0)
else:
    k -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate((set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}#'a', 'n', 't', 'i', 'c' 제외하고 딕셔너리를 만듬. 랜덤하게?!
    print("alpha:", alpha)
    #{'z': 0, 'y': 1, 's': 2, 'j': 3, 'e': 4, 'd': 5, 'l': 6, 'b': 7, 'q': 8, 'k': 9, 'o': 10, 'u': 11, 'h': 12, 'g': 13, 'p': 14, 'v': 15, 'm': 16, 'x': 17, 'r': 18, 'w': 19, 'f': 20}
    cnt = 0

    for _ in range(n):
        tmp = 0
        for c in set(input())-nece_chars:#set 연산
            print("c:",c)
            print("alpha c:", alpha[c])
            tmp |= (1 << alpha[c])#시프트 연산으로 해당 알파벳이 필요하다는 것을 저장. 2진수형태. ex) 1<<3 : 1000 (8)
            print("tmp:", tmp)
        input_chars.append(tmp)

    power_by_2 = (2**i for i in range(21))#generator,,,
    # print("power by 2:", list(power_by_2))#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]

    for comb in combinations(power_by_2, k):#2진수 조합으로 뽑음
        print("comb:", comb)
        test = sum(comb)#나온 조합의 합이 새롭게 배운 알파벳을 의미

        ct = 0
        for cb in input_chars: #&(and)연산을 하면 비트가 둘 다 1일 때 1을 저장.
            if test & cb == cb:# 비트연산 결과가 cb와 같다는 것은 적어도 cb의 1인 비트들은 test에 전부 포함되어 있다는 뜻
                ct += 1

        cnt = max(cnt, ct)

    print(cnt)