T = True
sub_multi = []
while T:
    a = int(input())
    if a == -1:
        T = False
        break
    sub_multi = []
    for i in range(1, a):
        if a % i == 0: #i가 a의 약수일 때
            sub_multi.append(i)
    sum = 0
    for j in range(len(sub_multi)):
        sum += int(sub_multi[j])
    str(sub_multi)
    sub_multi = list(map(str, sub_multi))
    
    if sum == a:
        print(a, "=", ' + '.join(sub_multi))
    else :
        print("{0} is NOT perfect.".format(a))