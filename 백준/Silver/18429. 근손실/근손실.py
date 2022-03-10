day, loss = map(int, input().split())
kit_list = list(map(int, input().split()))
check = [False] * day
result = []
my_weight = 500
count = 0

def DFS(L) :
    global count, my_weight

    if L == day :
        count += 1
        return
    else :
        for i in range(day) :
            if check[i] is False :
                check[i] = True                             #방문여부 체크(True)
                
                if my_weight + kit_list[i] - loss >= 500 :  #날짜가 지나면 my_weight-k만큼 감소 kit_list[i]만큼 증가
                    my_weight += kit_list[i] - loss
                    DFS(L+1)
                    my_weight -= kit_list[i] - loss         #백트랙킹 이므로 다시 보충
                    check[i] = False                        #방문여부 복구(False)
                else :              
                    check[i] = False                        #방문여부 복구(False)

DFS(0)
print(count)