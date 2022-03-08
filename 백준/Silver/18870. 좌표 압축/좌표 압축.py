import sys

n = int(input())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))
dic_num = {}
result_list = []

num_set = set(num_list)         #중복제거
new_list = list(num_set)        #중복 제거된 숫자 리스트
new_list.sort()                 #정렬하기

for i in range(len(new_list)) : 
    dic_num[new_list[i]] = i    #딕셔너리에 {숫자 값 : 정렬된 순서} 저장                  

for i in range(len(num_list)) :      #num_list에 순서에 맞게 순서 result_list에 추가
    print(dic_num[num_list[i]], end=" ")