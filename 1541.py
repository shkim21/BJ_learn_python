# import sys
# input = sys.stdin.readline

strings = input()

first = strings.split('-')
# print(first)

if first[0] =='':#맨 처음부터 -가 있는 경우
    second = '+'.join(first[1:])
    third = second.split('+')
    # second = first[1].split('+')
    # print(second)#[55, 50]
    hap = 0
    minus = 0
    for num in third:
        minus -= int(num)
    # print("minus:", minus)
elif len(first) == 1:
    second = first[0].split('+')
    hap =0
    minus = 0
    for num in second:
        hap += int(num)
else:
    second = first[0].split('+')
    hap = 0
    minus = 0
    for num in second:
        hap += int(num)
    third = '+'.join(first[1:])
    fourth = third.split('+')
    for num in fourth:
        minus += int(num)

print(hap-minus)