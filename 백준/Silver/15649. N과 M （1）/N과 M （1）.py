n, m = map(int, input().split())
result = []
check = [False] * (n+1)

def DFS(num) :
    if num == m :               #num이 m개를 다 만들었을때 출력
        print(" ".join(map(str, result)))
        return
    else :
        for i in range(1, n+1) :          #찾아야하는 숫자가 1부터 n까지이므로
            if check[i] == False :      #방문 여부가 False(미방문 인경우)
                check[i] = True         #방문 체크
                result.append(i)
                DFS(num+1)              #다음 찾을 숫자 넘겨줌
                check[i] = False
                result.pop()
DFS(0)