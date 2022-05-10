import sys

n, m = map(int, input().split())
data = list(map(int, input().split()))

sum_nums = 0
left, right = 0, 1
count = 0

while right <= n and left <= right :
    sum_nums = data[left:right]
    total = sum(sum_nums)

    if total == m :         #m과 같은 경우 카운트 증가
        count += 1
        right += 1          #찾았으니 right 포인트 오른쪽-> 이동
    #total이 아직 원하는 사이즈가 만들어 지지않았음 
    elif total < m :
        right += 1
    else :
        left += 1
    
print(count)