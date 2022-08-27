import sys

n = int(input())            #노드 수
start, end = map(int, input().split())
m = int(input())            #간선 수
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

def DFS(now, count) : 
    visited[now] = True             #방문한 노드 방문 처리
    count += 1                      #방문한 노드 카운트

    if now == end :                 #목표 노드에 도착하는 경우 카운트
        result.append(count)

    #현재 노드 now로부터 방문하지 않은 다음 노드를 방문하자
    for next in graph[now] :
        if visited[next] is False :
            DFS(next, count)

def solution() :
    #인접리스트 생성
    for _ in range(m) :
        node, line = map(int, input().split())
        graph[node].append(line)
        graph[line].append(node)
    
    DFS(start, 0)
    if len(result) == 0 :
        return -1
    else :
        return (result[0] - 1)


print(solution())

# 9         <-- 전체 사람의 수 n
# 7 3       <-- 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호
# 7         <-- 부모 자식들 간의 관계의 개수 m
# 1 2       <-- 넷째 줄부터는 부모 자식간의 관계
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6