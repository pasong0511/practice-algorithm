import sys


n = int(sys.stdin.readline().rstrip())
numList = []
for i in range(n) :
    line = int(sys.stdin.readline().rstrip())
    numList.append(line)

def solution(n, numList) :
    answer = 0
    numList.sort()          #정렬해야한다.

    #뒤에서부터 3개 비교해서
    #a + b 가 c보다 큰 경우를 찾는다
    for i in range(len(numList)-1, 1, -1) :
        a, b, c = numList[i-2], numList[i-1], numList[i]
        #print(a, b, c)
        if a + b > c :
            answer = a + b + c
            break
    
    if answer > 0 :
        return answer
    else :
        return -1
        
print(solution(n, numList))