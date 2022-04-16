import sys
from collections import deque

def BFS() :
    #1. 익은 토마토 먼처 찾기-익은 토마토 좌표는 큐에 다 넣어놓고 시작
    for i in range(hight) :
        for j in range(width) :
            if map_data[i][j] == 1 :
                dq.append([i, j])
    #2. 큐가 발때까지 익은 토마토(1)에서 인접한 0토마토를 순회
    #2. 익은 토마토의 기간을 day_list에 누적 기간을 체크해주기
    while dq :
        start_x, start_y = dq.popleft()
        
        for d in range(4) :
            next_x = start_x + dx[d]
            next_y = start_y + dy[d]
            
            if 0 <= next_x <= (hight - 1) and 0 <= next_y <= (width - 1) and map_data[next_x][next_y] == 0 :
                map_data[next_x][next_y] = 1
                day_list[next_x][next_y] = day_list[start_x][start_y] + 1
                dq.append([next_x, next_y])
    return day_list

def find_day_time() :
    flag = 1
    max_day = 0

    #토마토가 익지 않은게 있을 경우 : map_data에 0이 남아 있는 경우 -1
    for i in range(hight) :
        for j in range(width) :
            if map_data[i][j] == 0 :
                return -1
    
    #토마토가 다 익은 경우 익는데 걸리는 최대 날짜 반환
    for i in range(hight) :
        for j in range(width) :
            if day_list[i][j] >  max_day :
                max_day = day_list[i][j]
    return max_day


width, hight = map(int, input().split())
map_data = []
for i in range(hight) :
    data = list(map(int, input().split()))
    map_data.append(data)
    
dx = [-1, 0, 1, 0]          #위쪽 0, 오른쪽 1, 아래 2, 왼쪽 3
dy = [0, 1, 0, -1]

dq = deque()
visite_list = [[False] * width for _ in range(hight)]
day_list = [[0] * width for _ in range(hight)]

BFS()
print(find_day_time())