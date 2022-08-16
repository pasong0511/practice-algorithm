import sys
from collections import deque
import copy

n, m = map(int, input().split())
board = []
preCount = 0

#지도 입력
for i in range(n) :
    line = list(map(int, input().split()))
    board.append(line)

#2는 여러개가 있을 수 있다
#2인 바이러스를 찾으면서, BFS를 돌자 -> 떨어진 섬 찾기
#2로 덮일때 카운트를 세자
def BFS() :
    global preCount

    #bfs 준비
    dq = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    #2찾기
    copyBoard = copy.deepcopy(board)
    for i in range(n) :
        for j in range(m) :
            if copyBoard[i][j] == 2 :
                dq.append((i, j))

    #큐가 발때까지 반복
    while dq :
        nowX, nowY = dq.popleft()
        #print(nowX, nowY)
        for d in range(4) :
            nextX = nowX + dx[d]
            nextY = nowY + dy[d]

            #0인곳은 바꿀수있다, 중간에 1인 곳은 방문할수없다, 테두리로 나갈수없다
            if nextX < 0 or nextY < 0 or n <= nextX or m <= nextY :
                continue
            if copyBoard[nextX][nextY] == 0 :
                copyBoard[nextX][nextY] = 2
                dq.append((nextX, nextY))
            

    count = 0
    #안정역역 찾기(0) 찾기
    for i in range(n) :
            for j in range(m) :
                if copyBoard[i][j] == 0 :
                    count += 1
    preCount = max(count, preCount)


#벽 3개를 놓을 경우의 수 모두 찾기
#백트릭킹으로 이차원 리스트 돌면서, 0인곳 3개 뽑기
def wallMake(L) :
    if L == 3 :                         #3개만 뽑자
        BFS()
        return

    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :       #0인곳 찾아서 1만들어주기
                board[i][j] = 1
                wallMake(L+1)
                board[i][j] = 0         #빽트랙킹 완료 후 다시 0으로 복귀
    

wallMake(0)
print(preCount)