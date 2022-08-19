n, m = map(int, input().split())
board = []
for i in range(n) :
    line = list(map(int, input().split()))
    board.append(line)
chickComb = []
min_result = 2147000000

#조합 뽑기용 DFS
def DFS(m, L, start, homeList, chikenList, checkList) :
    global min_result
    #치킨가게 조합의 개수가 m과 같으면 종료
    if L == m :
        sum = 0
        for homePos in homeList :
            homeX, homeY = homePos
            distance = 2147000000            #각 집에서 치킨가게까지 얻을 수 있는 최소 거리 구해야함

            for chickPos in chickComb :
                chickX, chickY = chickPos
                distance = min(distance, abs(homeX - chickX) + abs(homeY - chickY))    #집에서 치킨 거리 구함
            sum += distance
        
        if sum < min_result :
            min_result = sum
    
    #치킨가게 조합 만들기
    else :
        for i in range(start, len(chikenList)) :
            if checkList[i] == False :
                checkList[i] = True
                chickComb.append(chikenList[i])
            
                DFS(m, L+1, i, homeList, chikenList, checkList)
                
                checkList[i] = False
                chickComb.pop()

def solution(n, m, board) :
    homeList = []
    chikenList = []
    global minDistanceSum

    #집과 치킨 가게 좌표 저장
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                homeList.append((i, j))
            elif board[i][j] == 2 :
                chikenList.append((i, j))

    checkList = [False] * len(chikenList)
    
    DFS(m, 0, 0, homeList, chikenList, checkList)
    print(min_result)

solution(n, m, board)