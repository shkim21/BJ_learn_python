T = int(input())

#0과 1을 저장하기 위한 배열 선언&초기화
zero = [1, 0]
one = [0, 1]

def fibonacci(n):
    lens = len(zero)#배열길이
    if n >= lens:#기존의 배열보다 들어온 숫자가 클 때
        for i in range(lens, n+1):
            zero.append(zero[i-1]+zero[i-2])#i번째 인덱스에 들어가는 값
            one.append(one[i-1]+one[i-2])
    #0, 1이 들어왔을 때 바로
    print("{} {}".format(zero[n], one[n]))#배열 인덱스 맞춰서 0,1 갯수 저장

for _ in range(T):
    N = int(input())
    fibonacci(N)