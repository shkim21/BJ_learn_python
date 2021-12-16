T = int(input())


#각각의 객체에 변수를 저장하기 위해서 클래스와 클래스 함수를 사용했다
class Fibo:
    def __init__(self):
        self.zero = 0
        self.one = 0

    def fibonacci(self, n):
        if self.zero != 0:
            return self.zero
        elif self.one != 0:
            return self.one

        if n == 0:
            self.zero += 1
            return
        elif n == 1:
            self.one +=1
            return
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


def fibonacci2(n):
    if n==0:
        zero[n] = 1
        return 1
    if n==1:
        one[n] = 1
        return 1 #list가 반환되면 안될듯?
    if zero[n] != 0:
        return zero[n]
    if one[n] != 0:
        return one[n]

    zero[n] = fibonacci2(n-1) + fibonacci2(n-2)
    one[n] = fibonacci2(n-1) + fibonacci2(n-2)
    return


for _ in range(T):
    N = int(input())
    zero = [0 for i in range(T)]
    one = [0 for i in range(T)]

    # num = Fibo()
    # a = num.fibonacci(N)
    # print(str(num.zero) + " " + str(num.one))
    a = fibonacci2(N)



