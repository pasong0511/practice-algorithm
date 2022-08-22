import sys

n = int(input())
word = []
for i in range(n) :
    word.append(input())

dic = {}
def solution(n, word) :
    #문자열을 키로 문자열 길이를 value로 딕셔너리 생성
    for w in word :
        dic[w] = len(w)
    
    #value 오름차순 정렬
    sortDic = sorted(dic.items(), key=lambda x:x[1])
    count = 0

    #i가 i+1과 비교했을때 접두사인지 체크
    for i in range(len(sortDic)) :
        for j in range(i+1, len(sortDic)) :
            #맨 앞꺼랑 슬라이스 해서 같은지 비교하자
            #하나라도 같은게 있으면 그 [i]는 접두어가 될수없다.
            if sortDic[i][0] == sortDic[j][0][:len(sortDic[i][0])] :
                count += 1      #접두어가 될수 없는 단어 개수 카운트
                break

    return len(sortDic)-count   #단어 길이 정렬 리스트에서 접두어가 될수없는 개수 빼줌

print(solution(n, word))

