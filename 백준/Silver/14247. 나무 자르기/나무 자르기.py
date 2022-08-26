import sys

n = int(sys.stdin.readline().rstrip())
firstHight = list(map(int, sys.stdin.readline().rstrip().split()))
growHight = list(map(int, sys.stdin.readline().rstrip().split()))

def solution(n, firstHight, growHight) :
    dic = {}
    treeSum = 0
    day = 0

    #성장하는 속도 value [0]를 기준으로 정렬을 한다
    for i in range(n) :
        dic[i] = [growHight[i], firstHight[i]]
    
    #성장하는 속도를 기준으로 오름차순 정렬
    sordDIc = sorted(dic.items(), key=lambda x: x[1])

    #초기 나무 높이[1] + (경과 일수 * 성장하는 속도)를 더해준다.
    for key, value in sordDIc :
        grow, first = value
        treeSum += first + (grow * day)
        day += 1
        
    return treeSum

print(solution(n, firstHight, growHight))

# 5
# 1 3 2 4 6
# 2 7 3 4 1