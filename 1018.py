N, M = map(int, input().split())

#2차원 배열
board = [[0 for col in range(M)] for row in range(N)]

ans1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
ans2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
# print(board)
for i in range(N):
    rows = input()
    # print("rows:", rows)
    for j in range(M):
        # print("rows[j]:", rows[j])
        board[i][j] = rows[j]

# print(board)

retouch = 0
retouch2 = 0
retouch_list = []

for i in range(N-7):
    for j in range(M-7):
        # second_board = board[i:i+8,j:j+8]
        # second_board = [[board[x][y] for x in range(i, i+8)] for y in range(j, j+8)]
        second_board = [row[j:j+8] for row in board[i:i+8]] #####2차원 배열 slicing!!
        # print("second_board:", second_board)

        retouch = 0
        retouch2 = 0
        for k in range(8):
            for m in range(8):
                # print("second_board[k][m]:", second_board[k][m])
                # print("ans1[k][m]:",ans1[k][m])
                # print("ans2[k][m]:",ans2[k][m])
                if second_board[k][m] != ans1[k][m]:
                    retouch += 1
                if second_board[k][m] != ans2[k][m]:
                    retouch2 += 1
        # print("retocuh:", retouch)
        # print("retocuh2:", retouch2)
        retouch_list.append(retouch)
        retouch_list.append(retouch2)

# print("retouch_list:", retouch_list)
print(min(retouch_list))

#문제풀이 아이디어
#갯수를 세는 배열 만들어서 최소값 출력하기
#for문 돌면서 8*8 배열 만들어서 ans1, ans2와 비교 후 다른 것 체크 후 갯수 저장
#리스트에 각각 ans1과 ans2와의 비교후 다른 것 갯수 저장하기 -> 최소값 반환 <- 정답!

#2차원 배열 슬라이싱!!