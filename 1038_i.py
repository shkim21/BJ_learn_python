def add_digit(digit,num):    #자리수에 따라 증가. 특정 자릿수까지 감소하는 숫자를 이어 붙이는 함수
    if digit==1:#1째자리 수 일때
        decreasing.append(num)
    else:#2이상일 땐 뒷자리에 숫자 추가해야 함
        for i in range(num%10):#<-바로 앞자리 숫자 구하기 위해
            add_digit(digit-1,num*10+i)#digit 감소시킨 후 재귀 호출함/ 원래 숫자인 num에 10곱해서 자리수 늘린후 i 더하기 ###이부분이 좀 어려움,,,


def backtracking(digit):    #백트래킹 시작
    for i in range(digit-1,10): #i : 실제 감소하는 수
        add_digit(digit,i)
    
decreasing=[]        #감소하는 숫자 리스트

for i in range(1,11):#1~10째자리 수까지 계산
    backtracking(i)

n=int(input())
print("decreasing:", decreasing)

if n>=len(decreasing):        #감소하는 숫자가 없을 때
    print(-1)
else:
    print(decreasing[n])

#이문제 풀이가 상당히 다양하다.. 구글링 5개 했는데 다 다름..!
#여러가지 풀이 방법이 있는듯