import sys

n = int(input())
numList = list(map(int, input().split()))
distMony = int(input())


def solution(n, numList, distMony) :
    left, right = 0, max(numList)
    gootMony = -1
    
    while left <= right :
        mid = (left + right) // 2

        calSum = 0
        for i in range(len(numList)) :
            #만약 원하는 예산이 mid 보다 큰 경우 최대 값은 mid
            if numList[i] >= mid :
                calSum += mid
            #만약 mid 이내라면 원하는 지역에서 원하는 만큼 준다.
            else :
                calSum += numList[i]

        #left, right 옮겨주기
        #만약 만든 예산이 여유가 있으면 돈 조금씩 더 나눠주도 된다.
        #left를 mid로 옮긴다.
        if calSum <= distMony :
            gootMony = mid              #나눠줄 예산 갱신
            left = mid + 1
        #만약 만든 예산이 부족해서 돈을 덜 나눠줘야한다.
        #mid가 right가 된다.
        else :
            right = mid - 1
            
    #각 예산에서 최대 값 구하기
    #적은 금액은 적은 금액만큼 주고, 큰 금액은 gootMony가 될것이다.
    answer = -1
    for num in numList :
        given = min(num, gootMony)      #gootMony보다 적은경우는 그냥 원한느 만큼만 줌
        answer = max(answer, given)     #그중에서 최대값 찾기

    print(answer)

solution(n, numList, distMony)