s = input()

def solution(s) :
    stack = []
    for i in s :
        #1. 여는 괄호 (, [ 나오면 스택에 쌓기
        if i == "(" or i == "[" :
            stack.append(i)
            continue
        #2. 닫는 괄호 ), ] 나오는 경우
        if i == ")" or i == "]" :
            #2-1. i = 닫는 괄호, 스택이 비어있는 경우 -> 거짓
            if len(stack) == 0 :
                return 0
            
            #2-2. i = 닫는 괄호, 스택 꼭대기가 여는 괄호인 경우
            if stack[-1] == "[" or stack[-1] == "(" : 
                #2-2-1. 닫는 괄호 ) 요청, 스택 꼭대기가 여는 괄호 (인 경우 2 push
                if i == ")" and stack[-1] == "(" :
                    stack.pop()                         #pop
                    stack.append(2)
                #2-2-1. 닫는 괄호 ] 요청, 스택 꼭대기가 여는 괄호 [인 경우 3 push
                elif i == "]" and stack[-1] == "[" :
                    stack.pop()
                    stack.append(3)
            
            #2-3. i = 닫는 괄호, 스택 꼭대기가 숫자인 경우
            else :
                #숫자 뽑자
                num = stack.pop()
                #2-3-1. 닫는 괄호 ) 요청, 숫자 뽑은 다음 스택 꼭대기가 닫는괄호 "("인 경우
                if len(stack) > 0 and i == ")" and stack[-1] == "(" :
                    stack.pop()
                    stack.append(2*num)
                elif len(stack) > 0 and i == "]" and stack[-1] == "[" :
                    stack.pop()
                    stack.append(3*num)
        #3. 스택 안에 연속해서 숫자가 나오는 경우 숫자 두개 팝해서 더한 후 스택에 다시 넣어줌 
        if len(stack) >= 2 and str(stack[-1]).isdigit() and str(stack[-2]).isdigit() :
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
    #4. 스택의 길이가 1이고 스택 내부에 들어 값이 숫자인 경우 반환
    if len(stack) == 1 and str(stack[-1]).isdigit() : 
        return stack[0]
    else :
        return 0

print(solution(s))