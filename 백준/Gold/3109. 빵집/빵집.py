r, c = map(int, input().split())
board = []
for _ in range(r) :
    board.append(list(map(str, input().strip())))

dx = [-1, 0, 1]     #많은 파이프 심으려면 우상향 접근 필요
dy = [1, 1, 1]      #오른쪽 위, 오른쪽, 오른쪽 아래
count = 0

def DFS(board, start_x, start_y) :
    global count
    #start_y가 오른쪽 끝에 도달하면 종료
    if start_y == c-1 :
        count += 1
        return True
    
    #오른쪽 대각선 위, 오른쪽, 오른쪽 대각산 아래 순서대로 깊이 우선 탐색
    for d in range(3) :
        next_x = start_x + dx[d]
        next_y = start_y + dy[d]

        #범위에 나가지 않도록
        if 0 <= next_x < r and 0 <= next_y < c :
            #벽이 아닌 경우 갈수 있음, 갈수 있는 곳은 체크
            if board[next_x][next_y] != 'x' and board[next_x][next_y] != 'o' :
                board[next_x][next_y] = 'o'     #현재 위치에 파이프 생성
                if DFS(board, next_x, next_y) : 
                    return True
    return False


def solution(board, r, c) :
    global count
    for i in range(r) :
        DFS(board, i, 0)
    return count

print(solution(board, r, c))