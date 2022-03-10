import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26
print("words:", words)

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함 default
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1
print("learn:", learn)


def dfs(idx, cnt):#인덱스로 돎. cnt 갯수를 인자로!
    global answer#global로 하는 이유? 함수 종료 따로, 함수 내에서 사용한 변수를 밖에서 사용할 수 있어서(?)
    print("idx:", idx, ", cnt:", cnt)
    print("learn:", learn)
    if cnt == k - 5:#종료조건/ cnt를 증가시키는 방식
        print("same")
        readcnt = 0
        for word in words:#n개의 입력단어들에 대해서
            check = True
            for w in word:#입력 글자 한글자씩 돌면서
                if not learn[ord(w) - ord('a')]:#인덱스로 접근. learn이 0이면
                    check = False
                    print("break")
                    break
            if check:#check가 false가 아니면. learn이 0이 아닐 때!
                readcnt += 1
        print("readcnt:", readcnt)
        answer = max(answer, readcnt)
        print("answer:", answer)
        return

    #조합을 dfs로 구했음... 레전드
    for i in range(idx, 26):#처음엔 0, 그 다음엔 for문 도는 범위가 다름
        if not learn[i]:#learn[i]가 0이면
            learn[i] = True #방문했다(?) 체크
            dfs(i, cnt + 1) #깊이 증가
            learn[i] = False #나오면 다시 방문체크 해제


dfs(0, 0)
print(answer)

#문자열(26글자) 조합이 시간이 많이 걸리는데, dfs로 직접 구현하면 괜춘한듯?!