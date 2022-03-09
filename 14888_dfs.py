# 백트래킹 (Python3 통과, PyPy3도 통과)
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

#경계값 체크위함
maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:#종료조건
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        # print("maximum:", maximum)
        # print("minimum:", minimum)
        return#반환값 없이 함수 종료시킴
    print(plus, minus, multiply, divide)
    print("total:", total)
    if plus:
        #재귀 돌면서 모든 경우 탐색 가능(?)
        dfs(depth +1, total + num[depth], plus -1, minus, multiply, divide)#길이 증가, total update, 깊이를 인덱스로 하여 접근
    if minus:
        dfs(depth +1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth +1, total * num[depth], plus, minus, multiply -1, divide)
    if divide:
        dfs(depth +1, int(total / num[depth]), plus, minus, multiply, divide-1)
dfs(1, num[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)