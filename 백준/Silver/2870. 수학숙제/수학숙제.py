n = int(input())
numList = []
for i in range(n) :
    word = input()
    
    answer = ''

    #라인 한줄 탐색하기
    for w in word :
        #숫자가 나오는 경우 stack에 넣기
        if w.isdigit() is True :
            answer += w
        #숫자가 아닌 경우 기존에 만들어진 문자들 저장, 이후 초기화
        else :
            if answer != '' :
                numList.append(int(answer))
            answer = ''
    #마지막 끝에 있는 경우도 체크
    if answer != '' :
        numList.append(int(answer))
    
numList.sort()
for num in numList :
    print(num)