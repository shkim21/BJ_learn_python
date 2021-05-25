N = int(input())

n = N
a = 1
for i in range(N):
    while n > 1:
        a = a*(n-i)
        n -= 1

print(a)


cache = {} #전역공간에 캐쉬로 쓸 dict 선언

#재귀함수를 이용한 방법
def factorial_recursive(n):
    global cache

    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * factorial_recursive(n-1)
        return cache[n]

#decorator를 이용해서 재사용성을 높이는 방법
def in_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper

@in_cache
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1


#reduce를 이용한 방법
from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
