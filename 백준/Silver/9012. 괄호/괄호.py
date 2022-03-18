n = int(input())

for _ in range(n) : 
    s = input()
    stack = []
    flage = True

    for i in s : 
        if i == "(" :
            stack.append(i)
            continue
        if len(stack) > 0 and i == ")" :        #스택이 비어있지 않고, )만나면 pop
            stack.pop()
        else :
            flage = False                       #스택이 비어있을때 요청하면 거짓

    if flage == False or len(stack) > 0 :       #스택이 비어있을때 요청하기나, 스택이 안비어있으면
        print("NO")
    else :
        print("YES")