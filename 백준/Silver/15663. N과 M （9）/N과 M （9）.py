n, m = map(int,input().split())
num_list = list(map(int, input().split()))
visited = [False] * n
result = []


num_list.sort()

def DFS(depth) :
    if depth == m :
        print(" ".join(map(str, result)))
        return
    else :
        overlap = 0                 #전에 쓰인 변수 값과 비교, 깊이가 다를 때마다 변수를 초기화
        for i in range(n) :
            if visited[i] is False and overlap != num_list[i]:
                visited[i] = True
                result.append(num_list[i])
                overlap = num_list[i]
                #print("overlap > ", overlap)
                DFS(depth+1)
                visited[i] = False
                result.pop()

DFS(0)
