n, targer_num = map(int, input().split())
num_list = []
for i in range(n) :
    num_list.append(int(input()))

min = 2147000000

def DFS(L, sum) :
    global min

    if sum >= targer_num  :     #합이 목표치와 크거나 같은 경우 최소값 비교
        if min > sum :
            min = sum
            #print(min)
            return
    if L == n :                 #숫자 리스트 개수만큼 다 돌면 종료
        return

    else :
        DFS(L+1, sum+num_list[L])
        DFS(L+1, sum)

DFS(0, 0)
print(min-targer_num)