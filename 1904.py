#문제의 핵심 : 조건(15746)으로 나눈 나머지 니깐 마지막에 나눌 게 아니라 연산할 때 넣어야 한다! 
#피보나치 문제 정형화 : DP - 배열 미리 선언(적당한 크기)해놓고 인덱스로 접근해서 업데이트하기. 
#for문 돌면서 업데이트

N = int(input())

#피보나치...

array = [0]*1000001
array[0] = 1
array[1] = 1


def fibonacci(n):
    # for i in range(2, n+1):
    #     array.append(array[i-1]+array[i-2])
    for i in range(2, n+1):
        array[i] = (array[i-1]+array[i-2]) % 15746
    return array[n]

print(fibonacci(N))