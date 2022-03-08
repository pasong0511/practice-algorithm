import sys

n = int(sys.stdin.readline())
word_list = []
word_dic = {}

for i in range(n) :
    word_list.append(input())                   #단어 입력

for i in range(n) :                             
    if word_list[i] not in word_dic.keys() :                #단어 중복 제외 하고 
        word_dic[word_list[i]] = len(word_list[i])     #딕셔너리로, 단어, 인덱스 입력

#람다로 item 단어길이 정렬[1]->key 사전 정렬[0]
sort_dic = sorted(word_dic.items(), key=lambda x: (x[1], x[0]))   

for i in range(len(sort_dic)):            #키 출력[i][0]
    print(sort_dic[i][0])