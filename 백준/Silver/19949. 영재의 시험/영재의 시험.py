num_list = list(map(int, input().split()))
result = []
n = 10
count = 0

def DFS(L) :
    global count

    if L == n :
        point = 0
        #10개의 시험 문제 중에서 몇개나 맞았는지 확인
        for i in range(n) :
            if result[i] == num_list[i] :
                point += 1

            #합산 점수가 5인 경우의 수 카운트
        if point >= 5 :
            count += 1
        return
    else :
        for i in range(1, 6) :          #1부터 5까지 선택
            #앞에서 뽑은 숫자가 연속해서 3개 사용한 숫자인지 확인
            if L > 1 and result[L-2] == result[L-1] == i :
                continue
            result.append(i)
            DFS(L+1)
            result.pop()


DFS(0)
print(count)