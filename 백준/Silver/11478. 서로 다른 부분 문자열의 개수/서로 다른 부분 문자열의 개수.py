data = input()
result = set()

for i in range(len(data)) :         #문자열 슬라이싱 시작 인덱스
    for n in range(i, len(data)) :  #문자열 슬라이싱 개수 
        result.add(data[i:n+1])

print(len(result))