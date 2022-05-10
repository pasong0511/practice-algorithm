import sys

n = int(input())
data = list(map(int, input().split()))
m = int(input())
count = 0

#left --> <-- right 이동
left, right = 0, n - 1
#정렬 해두고 시작
data.sort()
while left < right :
    sum_nums = data[left] + data[right]

    #m과 같은 경우에는 카운트 증가
    if sum_nums == m :
        count += 1
    
    #m보다 sum_nums이 작은 경우에 왼쪽 포인터가 -> 이동
    if sum_nums < m :
        left += 1
        continue
    #일반적인 경우 오른쪽 포인터가 <- 이동
    right -= 1

print(count)