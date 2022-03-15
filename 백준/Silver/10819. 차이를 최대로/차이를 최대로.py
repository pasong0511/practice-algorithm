n = int(input())
num_list = list(map(int, input().split()))
permu_list = []

visited = [False] * n
max_vlaue = -1

def DFS(depth) :
    global max_vlaue

    if depth == n :
        sum_num = 0
        for i in range(n-1) :
            num = abs(permu_list[i+1]-permu_list[i])    #순열로 만든 리스트에서 [i+1]-[i] 두개씩 빼줌
            sum_num += num
        if sum_num > max_vlaue :            #최대 값 찾기
            max_vlaue = sum_num
        return
    else :
        for i in range(n) :
            if visited[i] is False :
                visited[i] = True
                permu_list.append(num_list[i])
                DFS(depth+1)
                visited[i] = False
                permu_list.pop()

DFS(0)
print(max_vlaue)
