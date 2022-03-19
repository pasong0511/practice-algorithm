while True :
    string = input()
    if len(string) == 1 and string == "." :
        break
    stack = []
    flag = True
    for i in string :
        if i == "(" or i == "[" :
            stack.append(i)
            continue
        if i == ")" :
            if len(stack) > 0 and stack[-1] == "(" :
                stack.pop()
            else :
                flag = False
        if i == "]" :
            if len(stack) > 0 and stack[-1] == "[" :
                stack.pop()
            else :
                flag = False
        
    if flag == False or len(stack) > 0 :
        print("no")
    else :
        print("yes")