n = int(input())
key_list = list(map(int, input().split()))
m = int(input())
find_list = list(map(int, input().split()))
dic = {}

#키 리스트 값을 딕셔너리로 키 만들기
for key in key_list :
    if key not in dic.keys() :
        dic[key] = 1
        
for item in find_list:
    if item not in dic.keys(): 
        print(0)
    else: 
        print(1)