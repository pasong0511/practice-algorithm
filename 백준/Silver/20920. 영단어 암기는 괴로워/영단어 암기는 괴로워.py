import sys

n, m = map(int, input().split())
dic = {}
for _ in range(n) :
    line = input()

    if len(line) >= m :
        #키가 없는 경우 
        if line not in dic :
            dic[line] = [1, len(line), line]
        
        #키가 기존에 있는 경우 [0]에 있는 개수만 증가시키자
        else :
            dic[line][0] += 1
        
#개수, 길이, 알파벳 정렬
soredDic = sorted(dic.items(), key=lambda x:(-x[1][0], -x[1][1], x[1][2]))
#print(soredDic)
#키만 뽑아서 출력하기
for d in soredDic :
    print(d[0])

#자주 나오는 단어 앞에 배치
#길이가 길쑤록 앞에 배치
#알파벳 사전순으로 앞으로 배치

#길이가 M 이상인 단어만 외우기
#단어, 개수, 길이