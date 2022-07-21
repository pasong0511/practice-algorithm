#2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
def divided(p) :
    left_count = 0
    right_count = 0
        
    for i in range(len(p)) :
        if p[i] == "(" :
            left_count += 1
        else :
            right_count += 1
        
        #개수가 같은 경우 반환
        if left_count == right_count :
            return p[:i + 1], p[i + 1:]
        
#3. 문자열 u가 "올바른 괄호 문자열" 체크
def check(u) :
    stack = []
    result = []
    for i in u :
        print(i)
        #(가 오면 무조건 스택에 넣는다.
        if i == "(" :
            stack.append(i)
        #)가 오는 경우 스택을 확인한다
        # - 꼭대기에 (가 있으면 pop해주고 True를 반환한다.
        # - )차례인데 스택이 비어있는 경우 잘못된 경우 False를 반환한다.
        else :
            if len(stack) == 0 :
                return False
            stack.pop()
        return True
        
def solution(p):
    answer = ''
    
    #1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == '' : 
        return ''
    
    #2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    #u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열 가능
    u, v = divided(p)       #u : 균형잡힌 괄호 문자열, v : 는 빈 문자열
    
    #3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    #3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    if check(u) is True :
        return u + solution(v)
    
    #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else :
        answer += "("           #4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        answer += solution(v)   #4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        answer += ")"
        
        for i in u[1:len(u)-1] :    #4-4. u의 첫 번째와 마지막 문자를 제거하고
            if i == "(" :
                answer += ")"       #나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            else :
                answer += "("   #4-5. 생성된 문자열을 반환합니다.
        
    return answer

#(와 )의 개수가 같으면 균형잡힌 괄호
#(와 )의 짝이 맞는 경우 올바른 괄호

