import sys
sys.setrecursionlimit(10000)

T = int(input())

def DFS(current_x, current_y) :
    global count

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    board[current_y][current_x] = 0         #이미 지나간 곳은 방문처리
    count += 1                              #한 블록 지나갈때마다 카운트

    for d in range(4) :
        next_x = current_x + dx[d]
        next_y = current_y + dy[d]

        if 0 <= next_x < width and 0 <= next_y < hight and board[next_y][next_x] == 1:
            DFS(next_x, next_y)


for tc in range(T):
    width, hight, n = map(int, input().split())
    board = [[0] * width for _ in range(hight)]
    result = []
    for _ in range(n):
        x, y = map(int, input().split())
        board[y][x] = 1

    for x in range(width) :
        for y in range(hight) :
            if board[y][x] == 1 :
                count = 0                   #지나가는 블록 개수 카운트
                DFS(x, y)
                result.append(count)        #블록 개수를 리스트에 넣어줌
    print(len(result))                      #블록 개수의 길이가 영역 개수

#배추들이 몇군데 퍼져있는지 조사해라
#DFS 띄어져 있는 영역 찾기
#반복문으로 1인곳만 넘기기
#방문한 곳은 1처리