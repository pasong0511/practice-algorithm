s = input()
alpha_dic = {}

#아스키코드 이용해서 a~z까지 알파벳 만들기
for i in range(26) :
    alpha_dic[chr(97+i)] = 0

#딕셔너리에 개수 누적
for i in s :
    alpha_dic[i] += 1

for item in alpha_dic.values() :
    print(item, end=" ")