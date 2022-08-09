from collections import deque

#5, 7
M, N, K = map(int, input().split())

#1. 맵 생성
board = [[0] * N for _ in range(M)]     #갈수 있는 곳은 0

#2. 맵에 사각형 그리기
for _ in range(K):
    leftX, leftY, rightX, rightY = map(int, input().split())
    #일반적인 좌표는 왼쪽 위가 0, 0부터 시작하니 이에 맞게 변환
    for i in range(M-rightY, M-leftY):
        for j in range(leftX, rightX):
            board[i][j] = 1             #갈수 없는 곳은 1

def BFS(startX, startY) :
    dq = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # global fildWidth

    #1. 시작잠 넣기
    dq.append((startX, startY))
    board[startX][startY] = 1           #재방문 막기 위해 1처리
    count = 1                           #영역의 개수 카운트용

    while dq :
        nowX, nowY = dq.popleft()
        
        for d in range(4) :
            nextX = nowX + dx[d]
            nextY = nowY + dy[d]

            if 0 <= nextX < M and 0 <= nextY < N and board[nextX][nextY] == 0 :
                dq.append((nextX, nextY))
                board[nextX][nextY] = 1
                count += 1              #방문할때마다 카운트
    return count

fildWidth = 0
fildWidthList = []
#3. BFS 탐색
for i in range(M) :
    for j in range(N) :
        #0인곳만 방문해라
        if board[i][j] == 0 :
            fildWidthList.append(BFS(i, j))
            fildWidth += 1

print(fildWidth)
fildWidthList.sort()
print(*fildWidthList)

#크기 m * n
#k개의 직사각형 그림