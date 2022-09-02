import sys

n = int(input())
color = input()

blueCount = 0
redCount = 0
#이전꺼랑 다음꺼랑 비교했을 때 다르면 카운트
preColor = ''
for color in color :

    #이전꺼랑 현재꺼를 비교한다.
    if color != preColor :

        #다른 경우 작업 개수 증가
        if color == "B" :
            blueCount +=1
        else :
            redCount += 1

    #다른 경우 preColor 저장 색 변경
    preColor = color

minCount = min(blueCount, redCount)
print(minCount + 1)




#해결한 경우 파란색
#해결하지 못한 경우 빨간색