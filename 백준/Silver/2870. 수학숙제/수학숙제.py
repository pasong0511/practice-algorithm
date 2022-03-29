import re

n = int(input())
num_list = []
transed_list = []

for test_case in range(n) : 
    input_string = input()
    regex = re.compile("([0-9]+)")      #숫자 추출
    transed_list = regex.findall(input_string)      #추출한 숫자 리스트로 반환
    transed_list = list(map(int, transed_list))     #정렬, 0제거 위해서 int 형변환
    
    num_list += transed_list            #정규식으로 숫자 추출 한거 list에 추가

num_list.sort()                         #오름차순정렬(비 내림차순정렬)

for num in num_list :                   #출력
    print(num)