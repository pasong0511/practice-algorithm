import sys
input = sys.stdin.readline

#투포인터
n = int(input())
m = int(input())
num_list = list(map(int, input().split()))

#1. 투포인터를 쓰기 위해서는 정렬되야함
num_list.sort()
count = 0
start, end = 0, n-1     #시작은 왼쪽 끝과 오른쪽 끝

#2. #1 2 3 4 5 6 7
#    ↑           ↑    이렇게 놓고 시작

while start < end :
    #합이 m과 같은 경우 : start -> <- end 
    if num_list[start] + num_list[end] == m :
        count += 1
        start += 1      #찾은 경우 start -> 이동
        end -= 1        #찾은 경우 end <- 이동

    #합이 m보다 큰 경우 : <- end로 값을 줄여줌
    elif num_list[start] + num_list[end] > m :
        end -= 1
    #합이 m보다 작은 경우 : start ->로 값을 늘려줌
    else :
        start += 1
    
print(count)