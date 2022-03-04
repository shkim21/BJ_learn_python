n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

# print("first triangle:", triangle)

for i in range(1, n):#1, 2, 3
    # print("i:", i)
    length = len(triangle[i])#2, 3, ,,
    # print("length:", length)
    triangle[i][0] += triangle[i-1][0]#맨 앞
    triangle[i][-1] += triangle[i-1][-1]#맨 마지막
    if length > 2:
        for j in range(1, length-1):
            # print("j:", j)
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    # print("triangle:", triangle)

print(max(triangle[-1]))