n = int(input())
operator_list = list(map(str, input().split()))
visited = [False] * 10

min_value = ""
max_value = ""

def compared_operator(item1, item2, oper) :     # 부등호 조건이  만족할 때만 작동
    if oper == "<" :
        return item1 < item2
    if oper == ">" :
        return item1 > item2

def DFS(depth, string) :
    global min_value
    global max_value

    if depth == n + 1:                  #<--- 여기 들어오는 애들은 최소 연산자에는 맞는 애들만 들어오는 것임
        if len(min_value) == 0 :        #맨처음 나타나는 값이 최소, 마지막 저장되는 것이 최대
            min_value = string
        else :
            max_value = string
        return
    else :
        for i in range(10) :
            if visited[i] is False :
                #깊이가 0이여서 0개 선택할때 or 부등호가 맞는 경우 재귀 가능
                if depth == 0 or compared_operator(string[-1], str(i), operator_list[depth-1]) : 
                    visited[i] = True
                    DFS(depth + 1, string + str(i)) #선택한 숫자 문자열로 붙여주기
                    visited[i] = False
DFS(0, "")

print(max_value)
print(min_value)