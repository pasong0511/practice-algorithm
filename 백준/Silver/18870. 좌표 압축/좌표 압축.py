import sys

n = int(input())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))
dic_num = {}
result_list = []

num_set = set(num_list)             #중복제거
none_overlap = list(num_set)        #중복 제거된 숫자 리스트 생성
none_overlap.sort()                 #중복 제거된 리스트 정렬하기

for i in range(len(none_overlap)) :
    dic_num[none_overlap[i]] = i    #딕셔너리에 {숫자 값 : 정렬된 순서} 저장                  

for i in range(len(num_list)) :             #딕셔너리에 숫자에 대한 정렬된 순서 저장되어 있으니
    print(dic_num[num_list[i]], end=" ")    #num_list에 맞게 출력