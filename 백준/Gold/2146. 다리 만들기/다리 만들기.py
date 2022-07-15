import sys
from collections import deque

n = int(input())
map_data = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = sys.maxsize

#섬의 번호 구분
def BFS_separate(start_x, start_y, map_data, number) :
    dq = deque()

    #1인 시작점 넣기, 섬의 번호를 나누기 위해서 보드에 체크
    dq.append((start_x, start_y))
    map_data[start_x][start_y] = number     #섬에 번호 부여

    while dq :
        now_x, now_y = dq.popleft()

        #4방향 탐색
        for d in range(4):
            next_x = now_x + dx[d]
            next_y = now_y + dy[d]

            #범위 내에 있을 때 섬(1)만 방문해서 number로 변경
            #1인곳만 방문할것이다!
            if 0 <= next_x < n and 0 <= next_y < n and map_data[next_x][next_y] == 1:
                map_data[next_x][next_y] = number       #섬(1)에 섬 번호(number) 부여
                dq.append((next_x, next_y))

#섬이 번호로 구분되어 진 현재 경우 섬 번호(iland)와 다른 섬의 번호의 거리를 찾는다
def BFS_short(start_x, start_y, map_data, iland) :
    global answer
    dq = deque()
    distance_list = [[-1] * n for _ in range(n)]         #거리 저장 리스트 생성

    dq.append((start_x, start_y))                       #큐에 시작점 추가
    distance_list[start_x][start_y] = 0                 #현재 시작점을 다시 방문하지 않기 위해서 0으로 변경

    while dq :
        now_x, now_y = dq.popleft()

        for d in range(4) :
            next_x = now_x + dx[d]
            next_y = now_y + dy[d]

            if 0 <= next_x < n and 0 <= next_y < n :
                # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
                #거리가 -1(거리 미계산)과 0(현재섬 출발점)이 아닌경우, 현재 섬 번호(iland)가 아닌 경우 최소 거리값 체크
                if map_data[next_x][next_y] > 0 and map_data[next_x][next_y] != iland :
                    answer = min(answer, distance_list[now_x][now_y])       #최소 거리 갱신
                    return

                #바다(0)인 경우 distance를 1씩 늘린다.
                if map_data[next_x][next_y] == 0 and distance_list[next_x][next_y] == -1 :
                    distance_list[next_x][next_y] = distance_list[now_x][now_y] + 1
                    dq.append((next_x, next_y))



def solution(n, map_data) :
    global answer
    number = 2
    
    #1. 각 섬을 구분하기 위해서 시작점인 1을 찾자, 그리고 섬의 번호(number)를 부여하자
    for i in range(n) :
        for j in range(n) :
            if map_data[i][j] == 1 :            #섬의 시작점을 하나 찾았다! number를 부여해보자
                BFS_separate(i, j, map_data, number)
                number += 1                     #섬에 부여할 번호 증가

    iland_count_end = number-1      #섬 부여번호는 1부터 iland_num까지

    #2. 섬의 번호가 부여되어 섬을 구분할 수 았다.
    #- 섬을 구분하고 바다의 거리를 구하여 거리를 측정한다.
    #- 다시 BFS 시작
    for iland in range(1, iland_count_end+1) :              #섬의 번호의 좌표가 시작점이 된다.
        for i in range(n) : 
            for j in range(n) :
                if map_data[i][j] == iland :                #0아닌 섬 번호가 시작점
                    BFS_short(i, j, map_data, iland)
    
    return answer

print(solution(n, map_data))


#https://www.acmicpc.net/problem/2146