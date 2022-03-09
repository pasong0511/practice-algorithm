n, m = map(int, input().split())
result = []
check = [False] * (n+1)

def DFS(num, s) :
    if num == m:
        print(" ".join(map(str, result)))
        pass
    else :
        for i in range(s, n+1) :        #찾아야하는 숫자가 1부터 n까지이므로
            if check[i] == False :      #방문 여부가 False(미방문 인경우)
                check[i] = True         #방문 체크
                result.append(i)
                DFS(num+1, i+1)              #다음 찾을 숫자 넘겨줌
                check[i] = False
                result.pop()

DFS(0, 1)