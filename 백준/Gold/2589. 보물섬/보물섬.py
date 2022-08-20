import sys
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n) :
    line = input()
    temp = []
    for j in line :
        temp.append(j)
    board.append(temp)


def BFS(startX, startY) :
    dq = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    maxCount = 0

    #각 시작점마다 distanceList 생성
    distanceList = [[0] * m for _ in range(n)]

    dq.append((startX, startY))
    distanceList[startX][startY] = 1

    while dq :
        nowX, nowY = dq.popleft()

        for d in range(4) :
            nextX = nowX + dx[d]
            nextY = nowY + dy[d]

            if 0 <= nextX < n and 0 <= nextY < m and board[nextX][nextY] == "L" and distanceList[nextX][nextY] == 0 :
                dq.append((nextX, nextY))
                distanceList[nextX][nextY] = distanceList[nowX][nowY] + 1
                if maxCount < distanceList[nextX][nextY] :
                    maxCount = distanceList[nextX][nextY]
    return maxCount


def solution(n, m, board) :
    result = 0
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 'L' :
                result = max(result, BFS(i, j))
    
    print(result-1)

solution(n, m, board)