import sys

n, m = map(int, sys.stdin.readline().split())
sList = []

for _ in range(n) :
    sList.append(sys.stdin.readline().rstrip())

def solution(n, m, sList) :
    count = 0
    
    for _ in range(m) :
        word = sys.stdin.readline().rstrip()
        for s in sList :
            if word == s[:len(word)] :
                count += 1              #1개라도 있으면 카운트 이므로, 더이상 볼필요없다
                break
    
    return count

print(solution(n, m, sList))

# 5 10 <-- n, m

# baekjoononlinejudge   <-- s
# startlink
# codeplus
# sundaycoding
# codingsh   <-- s

# baekjoon
# star
# start
# code
# sunday
# coding
# cod
# online
# judge
# plus