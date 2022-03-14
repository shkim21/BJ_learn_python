n = int(input())

dec = []
if n > 1022:
    print(-1)
else:
    for num in range(10000000001):
        num_s = list(str(num))
        length = len(num_s)
        cnt = False
        # print("mun_s:", num_s)
        for i in range(length-1):#
            if num_s[i] <= num_s[i+1]:
                cnt = True
                break

        if not cnt:
            dec.append(num)
    # print('dec:',dec)
    # print(len(dec))
    print(dec[n])

#N의 범위는 1000000이지만, 1~9까지 만들 수 있는 최대 자연수는 9876543210 이다.
#이것을 for문으로 전부 돌리기는 힘들다...! 시간 초과날듯

#조합을 이용하거나,
#백트랙킹,,,

#1자리 수부터 10자리 수까지 앞자리보다 작은 숫자들만 이어 붙여준다면 불필요한 연산을 획기적으로 줄일 수 있다.
