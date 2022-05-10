import sys

n = int(input())
data = list(map(int, input().split()))
data.sort()

left, right = 0, n-1

result = data[left] + data[right]
result_left = data[left]
result_right = data[right]

while left < right :
    sum_nums = data[left] + data[right]
    
    #0 그 자체인 경우 -> 이보다 가까울수 없다!
    if sum_nums == 0 :
        print(data[left], data[right])
        break 
    
    #기존에 구했던 값이 보다 현재 구한 절대값이 더 적은 경우 - 현재 구한 절대값으로 교체
    if abs(sum_nums) < abs(result) :
        result = sum_nums
        result_left = data[left]
        result_right = data[right]

    if sum_nums < 0 :           #합이 음수인 경우 0에 가까워 질수있도록 왼쪽을 -> 이동 
        left += 1
    else :                      #합이 양수인 경우 0에 가까워질 수 있도록 오른쪽 <- 이동
        right -= 1

print(result_left, result_right)