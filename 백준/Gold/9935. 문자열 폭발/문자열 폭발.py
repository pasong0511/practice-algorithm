string = input()
bomb_string = input()

stack = []                      #스택에 입력문자열 string 하나씩 담음
bomb_len = len(bomb_string)     #폭발 문자의 길이

for i in range(len(string)) :   
    stack.append(string[i])     #스택에 입력 문자열 하나씩 담음

    #스택 꼭대기와 폭발 문자열 끝이 같은 경우
    #스택 꼭대기에서 폭발 문자 길이만큼 자른 문자열과 폭발 문자열 비교
    if stack[-1] == bomb_string[-1] and "".join((stack[-bomb_len:])) == bomb_string :
        del stack[-bomb_len:]   #같은 부분분 길이만큼 제거

result = "".join(stack)

if result == "" :
    print("FRULA")
else :
    print(result)