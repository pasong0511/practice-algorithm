import sys

n = int(input())
stack = []
result = 0
for i in range(n) :
    line = list(map(int, input().split()))
        
    #1이 나오면 -1해서 무조건 스택에 넣기
    if  line[0] == 1 :
        point, time = line[1], line[2]

        if time - 1 == 0 :      #첨부터 뺏을때 0인경우 넣지도 않음
            #print("겟포인트", [point, time-1])
            result += point
        else :                  #뺏을때 0이 아닌 경우 스택에 넣음
            stack.append([point, time-1])
            #print("스택에 넣기", stack)

    #0이 나오면 top에 있는거 -1 해주기
    #0인 경우 pop해주기
    else :
        if len(stack) > 0 :
            stack[-1][1] -= 1               #꼭대기에 있는 time감소 -1해주기
            #print(stack)

            if stack[-1][1] == 0 :          #감소했는데, 0이면 다 했으니까 pop해버림 
                getPoint = stack.pop()
                result += getPoint[0]
                #print("겟포인트", getPoint)

print(result)

#최근에 나온 순서대로, 나오면 바로함
#새로운 과제 나오면, 새로운 과제 진행
#새로운 과제 나오면, 이전꺼 다시함

# 3
# 1 100 3
# 0
# 0

# 5
# 1 10 3
# 0
# 1 100 2
# 1 20 1
# 0