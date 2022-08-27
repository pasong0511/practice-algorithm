import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numList = []

for i in range(n) : 
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    numList.append(line)

qn = int(sys.stdin.readline().rstrip())
qerey = []
for i in range(qn) : 
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    qerey.append(line)

#이차원 누적합 만들기
def MatrixPresum(n, m, numList) :
    preSum = [[0] * m for _ in range(n)]

    #이차원 누적합 만들기
    for i in range(n) :
        for j in range(m) :
            #시작점은 preSum[i][j] i = 0, j = 0, numList[0] 값
            if i == 0 and j == 0 :
                preSum[i][j] = numList[i][j]
            #맨 위쪽, 즉 i가 0인 경우에는 1차원 preSum과 같은 형태
            #preSum[i][j]는 numList[i][j] + preSum[i][j-1]을 누적합 해준다.
            elif i == 0 and j != 0 :
                preSum[i][j] = numList[i][j] + preSum[i][j-1]
            #맨 오른쪽, 즉 j가 0인 경우 preSum 만들기
            #위에꺼 누적해서 더해주기
            elif i != 0 and j == 0 :
                preSum[i][j] = numList[i][j] + preSum[i-1][j]
            #누적합 위, 누적합 왼쪽 더하고, 대각선 빼줌
            else :
                preSum[i][j] = numList[i][j] + preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1]
    return preSum

#4개의 좌표 밭아서 계산하기
def calPosPreSum(preSumMat, a, b, c, d) : 
    #시작 좌표 0, 0 인경우, 시작점에서 c, d만큼 누적합을 기록
    if a == 0 and b == 0 :
        print(preSumMat[c][d])
    #a좌표가 0인 경우, 맨 위에 붙은 꼴
    elif a == 0 and b != 0 : 
        print(preSumMat[c][d] - preSumMat[c][b-1])
    #왼쪽 벽에서부터 시작
    elif a != 0 and b == 0 :
        print(preSumMat[c][d] - preSumMat[a-1][d])
    #오른쪽 벽에서 시작한만큼 빼줌, 위쪽 벽에서 시작한 만큼 빼줌, 겹친 부분 더하기
    else :
        print(preSumMat[c][d] - preSumMat[c][b-1] - preSumMat[a-1][d] + preSumMat[a-1][b-1])

def solution(n, m, numList, qerey) :
    preSumMat = MatrixPresum(n, m, numList)

    #4개의 좌표를 이용해서 누적합 박스 계산
    for q in qerey :
        a, b, c, d = q
        a, b, c, d = a-1, b-1, c-1, d-1         #0부터 시작하기 위해서 빼줌

        calPosPreSum(preSumMat, a, b, c, d)
        

solution(n, m, numList, qerey)