import sys
from collections import deque

n, m = map(int, input().split())
board = []
distancedList = [[0] * m for _ in range(n)]

for i in range(n) :
    line = input()
    temp = []
    for j in line :
        temp.append(int(j))
    board.append(temp)

def BFS(startX, startY) :
    #1. BFS 초기 선언
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    
    #2. BFS 초기값 넣기
    dq.append((startX, startY))
    board[startX][startY] = 0
    distancedList[startX][startY] = 1

    while dq :
        nowX, nowY = dq.popleft()

        for i in range(4) :
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]

            if 0 <= nextX < n and 0 <= nextY < m and board[nextX][nextY] == 1 :
                dq.append((nextX, nextY))
                board[nextX][nextY] = 0
                distancedList[nextX][nextY] = distancedList[nowX][nowY] + 1
    
    print(distancedList[n-1][m-1])

BFS(0, 0)

#1은 이동할수 있는 칸
#0인 이동할수 없는 칸
#0, 0부터 시작해서
#n-1, m-1 도착하는 최단거리