cal, n = map(int, input().split())
num_list = list(map(int, input().split()))
max = -1

def DFS(L, sum) :
    global max
    
    if L < n + 1:
        if sum < cal and max < sum :
            max = sum
    if L == n :
        return

    else :
        DFS(L+1, sum+num_list[L])       #사용한다
        DFS(L+1, sum)                   #사용하지 않는다

DFS(0, 0)
print(max)