#투포인터 풀이

n, s = map(int, input().split())

n_list = list(map(int, input().split()))

n_sum = [0] *(n)
n_sum[0] = n_list[0]
for i in range(1, n):
    n_sum[i] = n_sum[i-1] + n_list[i]

print(n_sum)

ans = 100000


def pointer(start, end, ans):

    if start == n-1:
        return
    
    if n_sum[start] - n_sum[end] >= s and ans > start-end:
        ans = start- end
        end += 1
    else:
        if start < n:
            start += 1
        else:
            end += 1

    pointer(start, end, ans)


pointer(1, 0, ans)
print("ans:", ans)


#시간, 메모리 초과 안 나는 방법 : 부분합을 저장해서 인덱스로 접근해서 빼면 그 사이의 합이 나온다!(아이디어)