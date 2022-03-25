import sys
from collections import deque

def BFS(start_x, start_y, map_data, row, colum) :
    dx = [-1, 0, 1, 0]      #top, right, bottom, light
    dy = [0, 1, 0, -1]

    dq = deque()

    distance_list = [[0] * colum for _ in range(row)]

    #BFS초기 준비
    dq.append((start_x, start_y))           #1. 큐에 시작점 추가
    map_data[start_x][start_y] = 0          #2. 큐에 넣은 시작점은 방문처리

    while dq : 
        now_idx = dq.popleft()
        for i in range(4) :                         #4방향 이동(top-> right-> bottom-> light)
            next_x = now_idx[0] + dx[i]     #큐에 들어간 좌표 중 연결된 다음 x좌표[0]
            next_y = now_idx[1] + dy[i]     #큐에 들어간 좌표 중 연결된 다음 y좌표[1]

            #x좌표 내 and y좌표 내에서 이동 and 인접한 다음 방문할 곳이 길(1)인 경우 이동
            if 0 <= next_x <= (row-1) and 0 <= next_y <= (colum-1) and map_data[next_x][next_y] == 1:   
                map_data[next_x][next_y] = 0    #방문한 곳은 벽(0)처리
                distance_list[next_x][next_y] = distance_list[now_idx[0]][now_idx[1]] + 1   #현재값의 거리에 + 1
                dq.append((next_x, next_y))

    return distance_list


def solution() :
    row, colum = map(int, input().split())
    maps = []
    for i in range(row) :         #map 입력 받기
        m = input()
        temp = []
        for j in m :
            temp.append(int(j)) 
        maps.append(temp)
    
    distance_map = BFS(0, 0, maps, row, colum)

    if distance_map[row-1][colum-1] != 0 :
        answer = distance_map[row-1][colum-1] + 1
    else :
        answer = -1
    return answer

print(solution())

#미로찾기
#1은 이동할수 있는 칸
#0은 이동할 수 없는 칸
#0,0에서 n,m까지 이동할때 지나는 최소개의 칸 구하기