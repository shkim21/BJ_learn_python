alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N', 'O', 'P', 'Q','R','S','T','U','V','W','X','Y','Z']

def solution(name):
    answer = 0
    cnt = 0
    right = 0
    left = 0
    length = len(name)


    for i, n in enumerate(name):
        # right += 1
        # print("n:", n)
        # print("i:", i)
        left = length - i#중복일 때 처리를 못함
        # print("left:", left)
        if n == 'A':
            right += 1
            continue
        else:
            if name[i-1] != 'A' and i>0:#전 문자가 A가 아니면,,,
                right = 1
            cnt += min(left, right)
            idx = alphabets.index(n)
            if idx > 13:
                idx = 26 - idx
            # print("idx:", idx)
            cnt += idx
        # print("cnt:", cnt)
    # cnt -= 1
    # print("final cnt:", cnt)
    return cnt

# solution("JEROEN")
# solution("JAN")
print(solution("BAAAABB"))