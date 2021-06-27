N = int(input())

a = list(map(int, input().split()))
a.sort()#오름차순 정렬

print(a[0], a[N-1])