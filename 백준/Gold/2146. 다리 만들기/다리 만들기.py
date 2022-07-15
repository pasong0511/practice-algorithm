import sys
from collections import deque

n = int(input())
map_data = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = sys.maxsize

#섬의 번호 구분
def BFS(start_x, start_y, map_data, number, count) :
    dq = deque()
    count += 1

    #1인 시작점 넣기, 섬의 번호를 나누기 위해서 보드에 체크
    dq.append((start_x, start_y))
    map_data[start_x][start_y] = number

    while dq :
        now_x, now_y = dq.popleft()

        #4방향 탐색
        for d in range(4):
            next_x = now_x + dx[d]
            next_y = now_y + dy[d]

            #범위 내에 있을 때 섬(1)만 방문해서 number로 변경
            #1인곳만 방문할것이다!
            if 0 <= next_x < n and 0 <= next_y < n and map_data[next_x][next_y] == 1:
                count += 1
                map_data[next_x][next_y] = number
                dq.append((next_x, next_y))
    return count



def BFS_short(start_x, start_y, map_data, iland) :
    global answer
    dq = deque()
    distance_list = [[-1] * n for _ in range(n)]         #거리 저장 리스트

    dq.append((start_x, start_y))                       #큐에 시작점 추가
    distance_list[start_x][start_y] = 0

    while dq :
        now_x, now_y = dq.popleft()

        for d in range(4) :
            next_x = now_x + dx[d]
            next_y = now_y + dy[d]

            #범위 내에 있고
            if 0 <= next_x < n and 0 <= next_y < n :
                # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
                if map_data[next_x][next_y] > 0 and map_data[next_x][next_y] != iland :
                    answer = min(answer, distance_list[now_x][now_y])
                    return

                #바다(0)인 경우 distance를 1씩 늘린다.
                if map_data[next_x][next_y] == 0 and distance_list[next_x][next_y] == -1 :
                    distance_list[next_x][next_y] = distance_list[now_x][now_y] + 1
                    dq.append((next_x, next_y))

    #print("한번 찾음")
    #print(distance_list)



def solution(n, board) :
    global answer
    result = []
    number = 2
    #시작점인 1을 찾자
    for i in range(n) :
        for j in range(n) :
            if map_data[i][j] == 1 :            #섬의 시작점을 하나 찾았다! number를 부여해보자
                count = 0
                count = BFS(i, j, map_data, number, count)
                number += 1
    #print(map_data)

    iland_count_end = number-1      #섬 부여번호는 1부터 iland_num까지
    iland_count_start = iland_count_end - iland_count_end + 1

    for iland in range(iland_count_start, iland_count_end+1) :
        for i in range(n) : 
            for j in range(n) :
                # #0아니고,, 섬 번호가 시작점...
                if map_data[i][j] == iland :
                    #print(iland)
                    BFS_short(i, j, map_data, iland)
    
    return answer

print(solution(n, map_data))