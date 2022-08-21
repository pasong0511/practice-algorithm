import sys
s = input()
find = input()

def solution(s, find) :
    alphaStr = ""
    for i in range(len(s)) :
        if s[i].isalpha() is False :
            continue
        else :
            alphaStr += s[i]

    if find in alphaStr :
        return 1
    else :
        return 0


print(solution(s, find))
