import sys
from collections import deque

def solution() :
    n = int(sys.stdin.readline())
    queue = deque([i for i in range(1, n+1)])
    
    while len(queue) > 1 :
        queue.popleft()                     #맨 앞에꺼 버리기
        move_back = queue.popleft()         #맨 앞에 있는거 뒤로 옮기기
        queue.append(move_back)
    print(queue[0])

solution()