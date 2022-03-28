import re

def recursion(s) :
    regex = re.compile("(BUG)")
    transed_string = re.sub(regex, "", s)
    if s == transed_string :                #입력값이 변환된 값과 같은 경우 더이상 BUG 없음
        return transed_string               #반환 및 종료
    return recursion(transed_string)        #입력된 값이 변환된 값과 같지 않아 다시 변환 필요(재귀 처리)

while True :
    try :
        input_string = input()
        print(recursion(input_string))
    except :
        break