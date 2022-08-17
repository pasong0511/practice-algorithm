import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
countList = [0] * (n+1)

def BFS(node) :
    dq = deque()
    dq.append(node)

    visited = [False] * (n + 1)
    visited[node] = True
    #큐에 있는거 하나씩 빼면서 BFS 탐구
    while dq :
        nowNode = dq.popleft()

        for nextNode in graph[nowNode] :
            if visited[nextNode] is True :
                continue
            else :
                dq.append(nextNode)
                visited[nextNode] = True
    return visited.count(True)


for i in range(m) :
    dstn, src = map(int, input().split())
    graph[src].append(dstn)

for node in range(1, n + 1) :
    countList[node] = BFS(node)

maxNum = max(countList)

for i in range(len(countList)) :
    if countList[i] == maxNum :
        print(i, end=" ")