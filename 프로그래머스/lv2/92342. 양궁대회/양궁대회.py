from os import access

maxScore = 0
maxList = []

def ryanScore(index, score, n, apeach) :
    #종료 조건 1 : 화살을 쏠 수 있는 개수를 다 쐈다
    if n == 0 :
        #print(score)        #라이언이 만들어 낼 수 있는 점수의 경우의 수를 모두 다 만들자
        calScore(score, apeach)
        return 
    
    #종료 조건 2 : 0~10점간의 점수판을 다 도는 경우 종료
    if index == 11 :
        return
    
    #어피치 보다 점수가 + 1 높아야 한다.
    #또는 아예 0이 되어야 한다.
    #화살을 0개에서 어피치 + 1 만큼 쏘자
    sc = apeach[index]              #현재 index에서 어피치가 쐈던 화살의 개수를 저장
    #라이언은 0부터 sc+1개 만큼 쏴보는 경우의 수를 다 만든다.
    for i in range(sc+2) :
        score[index] = i            #0~n개까지 화살 쏜 개수 저장
        ryanScore(index+1, score, n-i, apeach)      #n-i는 화살을 쏜 개수이므로 다음번에 쏜 화살은 이번에 쓴 화살 개수에서 차감
        score[index] = 0            #다시 빽트랙킹    

def calScore(ryan, apeach) :
    global maxScore, maxList
    rScore = 0
    aScore = 0
    #라이언과 어피치의 인덱스의 화살의 개수를 비교하면서 큰 경우 점수를 주자
    
    #0~11인덱스의 과녁에 쏜 화살 개수를 비교
    for i in range(11) :
        #만약 둘다 0개 쏜 경우 둘다 0점 먹음
        if ryan[i] == 0 and apeach[i] == 0 :
            continue

        #과녁 점수 10-i에서 라이언이 더 많이 쏜 경우 -> 라이언이 점수 먹음
        if ryan[i] > apeach[i] :
            rScore += (10 - i)
        #과녁 점수 10-i에서 어피치가 더 많이 쏜 경우 -> 어피치가 점수 먹음
        else :
            aScore += (10 - i)
        
    #라이언의 점수의 최대 점수가 더 높을때 갱신(전체 경우의 수를 구했기 때문에, 라이언이 작을 수도있음)
    if rScore > aScore :
        diff = rScore - aScore

        #라이언 어피치 점수 차이가 큰 경우 최대 점수 차이 갱신
        if diff > maxScore : 
            maxScore = diff             #점수 갱신
            maxList = list(ryan)        #라이언 점수 리스트 갱신

        #최대 값이 같은 경우 낮은 점수를 많이 맞춘 경우 선택
        elif diff == maxScore :
            for i in range(11) :
                #낮은 점수를 많이 맞춘 경우 선택
                if ryan[-i] > maxList[-i] :
                    maxList = list(ryan)
                    break
                elif ryan[-i] < maxList[-i] :
                    break


def solution(n, apeach):
    temp = [0 for i in range(11)]
    ryanScore(0, temp, n, apeach)

    #라이언이 어피치보다 큰 점수가 없기 떄문에 maxList가 없는 경우 -1
    if len(maxList) == 0 :
        return [-1]
    else :
        return maxList

#K점
#어피치가 a발 맞혔고
#라이언이 b발을 맞춤
#더 많이 맞춘 사람이 k점을 가져간다
#동점인 경우 어피치가 k점 가져감

#문제풀이
#부분 수열 만들기
#모든 경우의수를 구해서 가장 요소가 많고 높은값을 선택