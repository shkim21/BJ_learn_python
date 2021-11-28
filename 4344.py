C = int(input())
for i in range(C):
    inputs = [x for x in input().split()]
    # print("inputs:", inputs)
    N = inputs[0]#5
    sum = 0
    for j in range(int(N)):
        sum += int(inputs[j+1])#1, 2, 3,,
    avg = sum / int(N)#평균 계산
    count = 0
    for k in range(int(N)):
        if int(inputs[k+1]) > avg:
            count += 1
    ans = count / int(N) * 100
    ans = round(ans, 3)
    print("{:.3f}%".format(ans))