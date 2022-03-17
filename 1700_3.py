n, k = map(int, input().split())
ordered = list(map(int, input().split()))

plug = []
cnt = 0

for i in range(k):#인덱스로 접근
    if ordered[i] in plug:#이미 있을 때 패쓰
        continue
    if len(plug) < n: #멀티탭에 아직 자리가 있을 때
        plug.append(ordered[i])
        continue

    idxs = []#이미 멀티탭에 꽂은 애들의 인덱스 저장. 가장 나중에 쓰는 애를 꺼내고 새로운 애를 집어넣음.
    for j in range(n):#멀티탭이 찼으니 길이가 n임
        try:
            idx = ordered[i:].index(plug[i])#멀티탭의 인덱스
        except:
            idx = 101#최대 입력 갯수가 100이니깐 최대값을 만들어 주기 위해서 101로 지정함
        idxs.append(idx)

    plug_out = idxs.index(max(idxs))#가장 나중 or 나중에 안 쓰는 애
    del plug[plug_out]
    plug.append(ordered[i])
    cnt += 1

print(cnt)


###xxxx 틀린 풀이
