N = int(input())
m = []
count = []
for _ in range(N):
    a, b = map(int, input().split())
    m.append(tuple((a, b)))
    sorted_m = sorted(m, key=lambda x:(x[1],x[0]))

print("m:", m)
print("sorted_m:", sorted_m)
for i in range(N):
    second = sorted_m
    r_count = 0
    for j in range(i+1, N):#index에러 날 수도. 리스트 지워가지고. <- 수정함
        if second[i][1] > second[j][0]:
            r_count += 1
            # length -= 1 #지우게 되면 앞으로 밀리는데 그러면 for문을 모든 경우에 돌릴 수 없음
    print("r_count:", r_count)
    count.append(N-r_count-i)

print("count:", count)
print(max(count))

#기존 생각 : 튜플로 입력값 받아서 정렬하고(첫번째 요소 오름차순, 두번째 요소도 오름차순)
#각 요소를 for문으로 돌면서 다음 요소가 첫번째 요소의 두번째 인자값보다 작으면 만든 임시 리스트에서 삭제. 갯수 구하려고. 갯수는 임시 리스트 길이로.

#고려하지 못한 상황 : 각 요소들에만 갯수를 구했으나 모든 상황을 만족하는 것을 한번에 구하지 못했음.

#잘못 생각한 것 : 회의 시작시간 순으로 정렬한 것.
#회의 끝나는 시간 순으로 정렬해야 기준으로 삼고 다음 항목이 끝나는 시간 보다 시작 시간이 빠른지 느린지 판단 가능하다
#end_time을 업데이트 해주는 것, 초기값 세팅하고.
