n, m = map(int, input().split())
numList = list(map(int, input().split()))

dic = {}

for i in numList :
    if i not in dic :
        dic[i] = 1
    else :
        dic[i] += 1

sortDic = sorted(dic.items(), key=lambda x:(-x[1], x[1]))

result = []
for key, value in sortDic :
    for i in range(value) :
        result.append(key)

print(*result)