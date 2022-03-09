import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
result = []

def DFS(L) :
    if L == m :
        print(" ".join(map(str, result)))
        return
    else :
        for i in range(1, n+1) :
            result.append(i)
            DFS(L+1)
            result.pop()

DFS(0)