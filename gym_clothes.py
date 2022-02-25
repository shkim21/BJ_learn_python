def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    reserve = sorted(reserve)

    for los in lost[:]:
        if los in reserve[:]:
            # print("remove!")
            lost.remove(los)
            reserve.remove(los)
    
    # print("lost1:", lost)
    wear = []
    for los in lost:
        # print("los:", los)
        for res in reserve:
            # print("res:", res)
            if res+1 == los or res-1 == los:
                wear.append(los)
                reserve.remove(res)
                break
    # print("waer:", wear)
    # print("lost:", lost)
    return n - len(lost) + len(wear)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(6, [1, 3, 5], [2, 4, 6]))
print(solution(5, [4, 2], [3, 5]))
print(solution(3, [1, 2], [2, 3]))

