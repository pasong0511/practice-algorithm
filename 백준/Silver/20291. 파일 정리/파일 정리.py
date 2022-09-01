import sys

n = int(input())
dataList = []

for _ in range(n) :
    line = input()
    dataList.append(line)

dic = {}
for data in dataList :
    cutData = data.split(".")
    if cutData[1] not in dic :
        dic[cutData[1]] = 1
    else :
        dic[cutData[1]] += 1


sortedDic = sorted(dic.items(), key=lambda x: x[0])

for key, value in sortedDic :
    print(key, value)

#파일을 확장자 별로 정리해서 몇개 있는지 알려줘
#확장자를 사전순으로 정리해줘

#점으로 분리
#분리한것을 딕셔너리 키로 만들기
