n = int(input())
goodCount = 0

for _ in range(n) :
    words = input()
    stack = []
    
    #스택에 하나씩 넣으면서 짝 맞는지 확인
    for i in range(len(words)) :
        if len(stack) > 0 :
            #현재값이랑, top값이랑 비교했을때 같은 경우 stack에서 top pop
            if words[i] == stack[-1] :
                stack.pop()
            else :
                stack.append(words[i])
        #t스택이 비어있는 경우
        else :
            stack.append(words[i])


    if len(stack) == 0 :
        goodCount += 1

print(goodCount)