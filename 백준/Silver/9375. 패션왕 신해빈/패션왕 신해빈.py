testCase = int(input())
for case in range(testCase) :
    n = int(input())
    dic = {}
    for i in range(n) :
        name, category = map(str, input().split())
        if category not in dic :
            dic[category] = 1
        else :
            dic[category] += 1
    
    #print(dic)

    answer = 1
    #각 의상의 개수가 a, b, c, ... 일 때 
    # 답이 {(a+1) * (b+1) * (c+1) * ... } - 1 이라는 것
    for key in dic.keys() :
        answer *= (dic[key] + 1)

    #안입는 경우만 빼줌
    print(answer-1)