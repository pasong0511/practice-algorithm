import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numList = list(map(int, sys.stdin.readline().rstrip().split()))
query = []
for i in range(m) :
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    query.append(temp)

def solution(n, m, numList, query) :
    
    #누적합 구하기
    prefixNum = [0] * n         #누적합 초기화
    prefixNum[0] = numList[0]   #0번째 값은 numList[0]의 0번째 값

    for i in range(1, n) :
        prefixNum[i] = prefixNum[i-1] + numList[i]

    
    #쿼리에 맞게 누적합 출력하기
    for qer in query :
        a, b = qer
        if a == 1 :
            answer = prefixNum[b-1]       #시작 값이 1인 경우 전체 합 = prefixNum의 마지막 값
        else :
            answer = prefixNum[b-1] - prefixNum[a-2]

        print(answer)

solution(n, m, numList, query)

# 5
# 1 3 2 4 6  <-- 처음 주어진  나무 길이
# 2 7 3 4 1  <-- 하룻마다 자랄 수 있는 나무 길이