n = int(input())
numList = ['1', '2', '3']
result = []
flag = False

def checkGood(num) :
    for i in range(1, len(num) // 2 + 1) :
        if num[-i:] == num[-i-i:-i] :
            return False
    return True

def backDFS(L) :
    global flag

    if flag is True :
        return

    if L == n :
        flag = True
        num = "".join(result)
        print(num)
        return
    
    else : 
        for i in range(3) :
            result.append(numList[i])
            if checkGood(result) :
                backDFS(L+1)
            result.pop()

backDFS(0)