n, m = map(int, input().split())

s = [] #순열을 쌓을 스택

def f():
    print("start f")
    if len(s) == m: #종료조건(길이가 m이랑 같으면!)
        print(' '.join(map(str, s)))#출력
        return#함수 종료!
    
    for i in range(1, n+1):#1, 2, 3,,, n
        if i in s:#함수가 다시 실행되었을 때 for문으로 매번 도는데, 중복된 것을 제거해줌 
        #스택에 존재하는지 여부로 판단함!
            continue

        s.append(i)
        print("s after append:", s)
        f()#다시 호출!
        print("end f, i:", i)
        s.pop()#맨 뒤에 요소를 제거해줌
        print("s pop after:", s)


f()