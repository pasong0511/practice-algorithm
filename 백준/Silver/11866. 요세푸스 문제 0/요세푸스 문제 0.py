import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, n+1)])
result = []
count = 1

while len(queue) > 1 :
    for _ in range(k-1) :
        queue.append(queue.popleft())
    result.append(queue.popleft())

result.append(queue.popleft())
print("<"+", ".join(map(str, result)) + ">")