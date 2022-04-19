import sys
def DFS(L, s) :
    global min_result
    if L == m :
        sum = 0
        #집의 좌표를 하나씩 꺼내서 피자집 좌표와 비교
        for j in range(len(home_position)) :
            x1 = home_position[j][0]
            y1 = home_position[j][1]
            distance = 2147000000
            #피자집 좌표를 하나씩 꺼내서 집과 피자거리 계산
            for x in check_combi :
                x2 = piza_position[x][0]
                y2 = piza_position[x][1]
                #피자 거리 최소값 저장
                distance = min(distance, abs(x1-x2) + abs(y1-y2))
            #피자 거리 최소값들 누적
            sum += distance
        if sum < min_result :
            min_result = sum
    else :
        #피자집 좌표 조합 구하기(m개 만들기)
        for i in range(s, len(piza_position)) :
            check_combi[L] = i
            DFS(L+1, i+1)


n, m = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]

home_position = []
piza_position = []

check_combi = [0] * m

min_result = 2147000000

for i in range(n) :
    for j in range(n) :
        #집 좌표 넣기
        if map_data[i][j] == 1 :
            home_position.append((i, j))
        #피자집 좌표 넣기
        elif map_data[i][j] == 2 :
            piza_position.append((i, j))

DFS(0, 0)
print(min_result)