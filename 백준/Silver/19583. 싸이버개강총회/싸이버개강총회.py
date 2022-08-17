import sys

inputStart, inputEnd, inputStream = map(str, input().split())
cutStart = list(map(int, inputStart.split(":")))
cutEnd = list(map(int, inputEnd.split(":")))
cutStream = list(map(int, inputStream.split(":")))
start = int(cutStart[0] * 60 + cutStart[1])        #초변환1
end = int(cutEnd[0] * 60 + cutEnd[1])              #초변환
stream = int(cutStream[0] * 60 + cutStream[1])   #초변환

dic = {}

for i in sys.stdin:
    inputTime, nick = i.rstrip().split()
    cutTime = list(map(int, inputTime.split(":")))
    time = int(cutTime[0] * 60 + cutTime[1])

    #개총 시작 전에 들어온 사람 체크
    if time <= start :
        dic[nick] = 1
    #개총 끝나고~스트리밍 끝나기 전까지 사람 +1
    elif end <= time and time <= stream :
        if nick in dic :
            dic[nick] += 1

result = 0
for key, val in dic.items() :
    if val >= 2 :
        result += 1

print(result)