n, m = map(int, input().split())
num_list = list(map(int, input().split()))

result = []
check = [False] * (n)
num_list.sort()

def DFS(L, start_index) :
    if L == m :
        print(" ".join(map(str, result)))
        return
    else :
        for i in range(start_index, n) :
            result.append(num_list[i])
            DFS(L+1, i)
            result.pop()

DFS(0, 0)