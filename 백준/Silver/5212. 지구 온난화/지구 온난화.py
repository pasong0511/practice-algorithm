import sys
import copy

n, m = map(int, input().split())
board = []
for _ in range(n) :
    line = input()
    temp = []
    for j in line :
        temp.append(j)
    board.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
newBoard = copy.deepcopy(board)     #새롭게 바다 채워넣을 보드 생성

def checkPos(nowX, nowY) :
    closeCount = 0

    for d in range(4) : 
        nextX = nowX + dx[d]
        nextY = nowY + dy[d]

        #왼쪽-1, 위-1 벽인 경우에는 카운트만 증가
        #오른m, 아래 n 벽인 경우에는 카운트만 증가 
        if nextX < 0 or nextY < 0 or n <= nextX or m <= nextY :  
            closeCount += 1
            continue
        #범위 내에 있고, 바다인 경우 카운트 증가
        if board[nextX][nextY] == "." :
            closeCount += 1

    #인접카운트가 3개 이상인 경우 now 좌표에 있는 값을 바다(.)로 변경해주기
    if 3 <= closeCount <= 4 :
        newBoard[nowX][nowY] = "."

#1. X 찾기
for i in range(n) :
    for j in range(m) :
        if board[i][j] == "X" :
            checkPos(i, j)          #2. 시작점 섬(X) 찾고 4방향 체크

#3. 출력에 맞게 바다 잘라주기
minRow = n - 1
maxRow = -1
minCol = m - 1
maxCol = -1

#땅인 경우만 생각해서 x, y의 최소 최대값 위치만 찾아준다.
for rowIdx, rowValue in enumerate(newBoard) :
    for colIdx in range(len(rowValue)) :
        if newBoard[rowIdx][colIdx] == 'X' :

            minRow = min(minRow, rowIdx)
            maxRow = max(maxRow, rowIdx)

            minCol = min(minCol, colIdx)
            maxCol = max(maxCol, colIdx)

#4. 좌표에 맞게 50년뒤 섬 지도 잘라주기
for i in range(minRow, maxRow + 1) :
    for j in range(minCol, maxCol + 1) :
        print(newBoard[i][j], end="")
    print()

#R*C 크기의 그리드
#'X'는 땅
#'.'는 바다
#50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨

#지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다