import sys

n = int(input())
num_list = [1, 5, 10, 50]
com_list = []
new_com_list = []
result = []

def DFS(L, start_index) :
    if L == n :
        new_com_list.append(com_list[:])
        return
    else :
        for i in range(start_index, len(num_list)) :
            com_list.append(num_list[i])
            DFS(L+1, i)
            com_list.pop()

DFS(0, 0)
for i in new_com_list :
    result.append(sum(i))

print(len(set(result)))
