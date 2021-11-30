inputstring = input()

dic = {}#문자별 갯수
for i in inputstring.upper():
    if i in dic:#existed
        dic[i] += 1
    else:
        dic[i] = 1

sorted = sorted(dic.items(), key=lambda x: (x[1],x[0]), reverse=True)#dic -> sort -> list, tuple

if len(sorted) == 1:#문자 하나 예외처리
    print(sorted[0][0])
else:
    if sorted[0][1] == sorted[1][1]:#정렬한 리스트 제일 첫 글자와 두번째 글자의 count가 같을 때-> 문제상황 처리
        print("?")
    else:
        print(sorted[0][0])


#####################인터넷 참고 코드
words = input().upper()
unique_words = list(set(words)) #입력받은 문자열에서 중복값을 제거 set: 중복제거

cnt_list = []
for x in unique_words:
    cnt = words.count(x) #count 함수 사용
    cnt_list.append(cnt) #갯수를 리스트에 저장. 위치가 동일함

if cnt_list.count(max(cnt_list)) > 1: #count 숫자 최대값이 중복되면  max함수 list
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list)) #count 숫자 최댓값 인덱스(위치) index 함수
    print(unique_words[max_index])#인덱스로 리스트 접근해서 출력


