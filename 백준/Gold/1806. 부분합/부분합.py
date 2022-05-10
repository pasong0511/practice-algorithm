n, m = map(int, input().split())
data = list(map(int, input().split()))

left, right = -1, 0
temp_sum = data[0]              #처음에는 하나 넣어줌
min_len = 100001

while right < n :
    if temp_sum >= m :
        if min_len > right - left :
            min_len = right - left
        left += 1
        temp_sum -= data[left]
    else :
        right += 1
        if right < n :
            temp_sum += data[right]

if min_len == 100001 :
    print(0)
else :
    print(min_len)