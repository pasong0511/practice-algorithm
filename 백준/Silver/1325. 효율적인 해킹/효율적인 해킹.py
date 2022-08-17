import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
countList = [0 for _ in range(n + 1)]

for i in range(m) :
    dstn, src = map(int, input().split())
    graph[src].append(dstn)

def BFS(startNode) :
    dq = deque()
    visited = [False] * (n + 1)
    visited[startNode] = True
    dq.append(startNode)
    count = 0
    #print("시작노드", startNode)
    
    #큐가 빌때까지
    while dq :
        nowNode = dq.popleft()          #팝하면서 방문한다
        count += 1
        #print("팝", nowNode)

        for nextNode in graph[nowNode] :
            if visited[nextNode] is True :
                continue
            else :
                dq.append(nextNode)     #다음 방문할 노드 큐에 넣기
                visited[nextNode] = True
    return count

#시작점 하나씩 뽑아서 노드 돌기
#시작점은 1에서 5까지 이다.
for startNode in range(1, n+1) :
    countList[startNode] = BFS(startNode)

#print(countList)
maxCount = max(countList)

for i in range(1, n+1) :
    if countList[i] == maxCount :
        print(i, end=" ")