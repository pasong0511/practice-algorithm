def DFS(L) :
    global count
    global flag
    global answer
    if L == m :
        count += 1
        if count == int(num) :
            answer = "".join(map(str, result))
            flag = True
        return
    else :
        for i in range(m) :
            if check[i] == False :
                check[i] = True
                result.append(s_list[i])
                DFS(L+1)
                check[i] = False
                result.pop()

while True :
    try : 
        string, num = input().split()
    except :
        break

    s_list = list(map(str, string))         #입력받은 string의 list화
    m = len(s_list)                         #m개 뽑음
    result = []                             #매번 순열로 만든 결과 저장
    check = [False] * m                     #순열은 중복방문 미허용으로 체크 필요
    count = 0
    answer = ''
    flag = False
    
    DFS(0)
    if flag is True :
        print(f'{string} {num} = {answer}')
    else :
        print(f'{string} {num} = No permutation')