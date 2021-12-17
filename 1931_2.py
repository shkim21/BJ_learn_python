N = int(input())
# m = [[0]*2 for _ in range(N)]
m = []
count = []
for i in range(N):
    a, b = map(int, input().split())
    m.append(tuple((a, b)))
    # m[i][0] = a
    # m[i][1] = b

sorted_m = sorted(m, key=lambda x:(x[1],x[0]))

# print("m:", m)
# print("sorted_m:", sorted_m)

end_time = sorted_m[0][1]
count = 1
for i in range(1, N):
    if end_time <= sorted_m[i][0]:
        # print("end_time:", end_time)
        # print("sorted_m:", sorted_m[i][0])
        # print("count:", count)
        count += 1
        end_time = sorted_m[i][1]

print(count)



#기존 생각 : 튜플로 입력값 받아서 정렬하고(첫번째 요소 오름차순, 두번째 요소도 오름차순)
#각 요소를 for문으로 돌면서 다음 요소가 첫번째 요소의 두번째 인자값보다 작으면 만든 임시 리스트에서 삭제. 갯수 구하려고. 갯수는 임시 리스트 길이로.

#고려하지 못한 상황 : 각 요소들에만 갯수를 구했으나 모든 상황을 만족하는 것을 한번에 구하지 못했음.

#잘못 생각한 것 : 회의 시작시간 순으로 정렬한 것.
#회의 끝나는 시간 순으로 정렬해야 기준으로 삼고 다음 항목이 끝나는 시간 보다 시작 시간이 빠른지 느린지 판단 가능하다
#end_time을 업데이트 해주는 것, 초기값 세팅하고.

#시간초과 원인 : sort를 for문 안에서 돌림,,;