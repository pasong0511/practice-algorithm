import sys
from collections import deque

def BFS(start) :
    count = 0               #방문 한 곳 카운트
    #1. 시작점 큐에 넣기
    dq.append(start)
    #2. 시작점 방문처리
    visited[start] = True

    #3. while dq 돌면서 한개씩 뽑으면서 방문하지 않은 곳 방문하기
    while dq :
        now = dq.popleft()

        #한개의 노드를 방문하면서, 그 노드에 연결되어 있는 다음 노드를 또 방문한다.
        #방문할때는 visited를 체크하면서, 방문하지 않은 경우에만 방문한다.
        for next in graph[now] :        #graph[now]는 이차원 리스트 중 한개
            if visited[next] is False : 
                dq.append(next)
                visited[next] = True
                count += 1              #4. 큐로 뽑아서 방문하게 되는 경우 카운트 증가

    return count


node_cnt = int(input())         #노드 개수
line_cnt = int(input())         #라인 개수

graph = [[] for _ in range(node_cnt + 1)]
visited = [False] * (node_cnt + 1)
dq = deque()

#1. 연결 사항을 확인해주는 인접 리스트 생성
for _ in range(line_cnt) :
    node, line = map(int, input().split())
    graph[node].append(line)
    graph[line].append(node)

#2. 시작점이 1이니 1부터 BFS 탐색을 시작한다.
print(BFS(1))