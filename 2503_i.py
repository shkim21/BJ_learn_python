# 2503, 숫자 야구
import sys
from itertools import permutations

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = list(permutations(n, 3))	# 순열로 3개씩 뽑음

t = int(sys.stdin.readline())

for _ in range(t):
    test, s, b = map(int, sys.stdin.readline().split())
    test = list(str(test))
    removed_cnt = 0     # 배열에서 제거된 튜플 개수
    print("test:", test)
    # num : 3개 리스트
    leng = len(num)
    print("leng:", leng)
    for i in range(leng):#모든 경우에 대해서
        s_cnt = b_cnt = 0   # 스트 개수, 볼 개수 0 초기화
        print("i:",i, "removed_cnt:", removed_cnt)
        i -= removed_cnt#list remove를 써서 그런건가 ㅇㅇ 제거했기 때문에. [:] 쓰면 안써도 될듯

        # 504개의 순열들을 돌면서 각각의 경우에 대한 스트라이크와 볼 수를 계산함 <- (시간초과 날 것이라 생각함,,,)
        for j in range(3):#각자리 수
            test[j] = int(test[j])
            if test[j] in num[i]:#있을 때
                if j == num[i].index(test[j]):#자리까지 같을 때 -> 스트라이크
                    s_cnt += 1
                else:#자리가 안 같을 때 -> 볼
                    b_cnt += 1
        print("s_cnt:", s_cnt, "b_cnt:", b_cnt)
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])# 스트라이크 개수, 볼 개수 다르면 배열에서 제거
            removed_cnt += 1

print(len(num))