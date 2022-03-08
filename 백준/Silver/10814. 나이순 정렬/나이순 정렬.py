import sys

n = int(sys.stdin.readline())
member_list = []

for i in range(n) :
    age, name = (sys.stdin.readline().rstrip().split())     #단어 입력
    member_list.append([int(age), name, int(i)])                      #리스트에 나이, 이름, 인덱스 저장

member_list.sort(key=lambda x:(x[0], x[2]))                 #나이[0] -> 인덱스[2] 정렬

for i in range(n) :
    print(member_list[i][0], member_list[i][1])             #나이[i][0], 이름[i][1] 출력