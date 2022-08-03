import sys
input = sys.stdin.readline


n, m = map(int, input().split())
dic_name = {}
dic_num = {}

for i in range(n) :
    name = input().rstrip()
    dic_num[int(i+1)] = name        #int(안덱스 번호) = 이름
    dic_name[name] = int(i+1)       #이름 = int(인덱스번호)

for i in range(m) :
    find = input().rstrip()
    #문자로 입력받음
    if find.isalpha() is True :
        print(dic_name[find])
    #숫자로 입력 받음
    else :
        print(dic_num[int(find)])
    