n, k = map(int, input().split())
ordered = list(map(int, input().split()))

taps = []#[False]*(n)
cnt = 0

for idx, o in enumerate(ordered):
    print("idx:", idx, "o:", o)
    print("taps:", taps)
    if o in taps:
        continue

    if len(taps) < n:#멀티탭 아직 다 안찼고, 안 꽂혀 있을 때
        taps.append(o)
        continue

    # else:#멀티탭 다 찼거나, 멀티탭에 있을 때
        # if o in taps:
        #     continue#이미 있을 때 pass
        # else:#멀티탭 다 찼는데 안 꽂음
            #그리디하게 우선순위 맞춰서 뽑아야함
    # print("idx:", idx)
    remain = ordered[idx+1:]
    # print("remain:", remain)
    find = False
    #안 쓰는거 있으면 먼저 뽑기
    print("taps[:]:", taps[:])
    for t in taps[:]:#복사본
        print("t:", t)
        if t not in remain:
            taps.remove(t)
            # print("t 안 씀!")
            find = True
            break# 안되면 조건문에 find =False 추가할 것
    # print("break 하고 여기 오나?")
    # print("taps:", taps)
    # taps.append(o)
    #2개 이상 쓰면 가장 나중에 쓰는 거 뽑기
    if not find:#못 찾았을 때
        # print("no find")
        tmp = []
        for t in taps[:]:
            for r in reversed(remain):#뒤에서부터 돔
                if r == t:
                    idx = list(reversed(remain)).index(r)
                    # print("idx:", idx)
                    tmp.append([r, idx])
        #인덱스가 낮은게 가장 나중에 쓰이는 것임
        sot = sorted(tmp, key = lambda x: x[1])
        # print("sot[0][0]:",sot[0][0])#가장 나중에 쓰이는 애
        taps.remove(sot[0][0])
        # print("taps:", taps)
    taps.append(o)
    cnt += 1


print(cnt)

#아니 반례들 다 맞는데 어디서 틀렸는지를 모르겠음...