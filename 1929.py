# import math

# no_list = []
# for i in range(M, N):
#     for j in range(2, int(math.sqrt(i))+1):
#         if i % j == 0:#배수
#             no_list.append(i)

# mylist = list(dict.fromkeys(no_list))

# for i in range(M, N):
#     if i not in mylist:
#         print(i)
    
M, N = map(int, input().split())

def is_prime_num(n):
    arr = [True] * (n+1)

    for i in range(2, n+1):
        if arr[i] == True:
            j = 2

        while (i*j) <= n:
            arr[i*j] = False
            j += 1
    return arr

arr = is_prime_num(N)

for i in range(M, N+1):
    if arr[i] == True:
        print(i)