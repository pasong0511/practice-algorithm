import sys

n = int(input())
sList = []

for _ in range(n) :
    sList.append(input())

#n개의 리스트에서 n개를 순열을 만들어라
def BACK(L, s, visited, result, recode) :
    #만들어진 문자열의 길이가 s와 같은 경우, 출력
    if L == len(s) :
        print("".join(result))
        return
    else :
        for i in range(len(s)) :
            if visited[i] is False :
                temp = result.copy()
                temp.append(s[i])
                if tuple(temp) not in recode :
                    visited[i] = True
                    result.append(s[i])
                    recode.add(tuple(temp))
                    BACK(L+1, s, visited, result, recode)
                    visited[i] = False
                    result.pop()

def solution(n, sList) :
    for s in sList :
        s = list(s)
        s.sort()
        visited = [False] * len(s)
        result = []
        recode = set()
        BACK(0, s, visited, result, recode)

solution(n, sList)

# 2
# abc
# acba

#abc로 만들수 있는 3개 뽑는 순열 딕셔너리로 저장하기
#acba로 만들 수 있는 4개 뽑는 순열 딕셔너리로 저장하기