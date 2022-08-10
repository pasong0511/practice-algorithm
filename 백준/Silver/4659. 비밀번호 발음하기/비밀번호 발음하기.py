def checkEssential(word) :
    flag = False
    for w in word :
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w =='u' :
            flag = True
    return flag

#모음이 3개, 자음이 3개연속으로 오면 안된다.
def checkRecurWord(word) :
    vowel = 0           #모음
    consonant = 0       #자음
    for w in word :
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w =='u' :       
            consonant = 0       #자음 초기화
            vowel += 1          #모음 카운트 +1
        else :
            vowel = 0
            consonant += 1
        
        if vowel >= 3 or consonant >= 3:
            return False
    return True

#같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
def checkSameWord(word) :
    stack = []
    wordList = list(word)
    stack.append(wordList[0])           #0번째꺼 넣기
    for i in range(1, len(word)) :      #1번째부터 끝까지 비교
        if stack[-1] != wordList[i] or (stack[-1] == 'e' and wordList[i] == 'e' ) or (stack[-1] == 'o' and wordList[i] == 'o' ) :   #꼭대기랑 현재꺼랑 비교해서 다른 경우
            stack.pop()                 #기존에 있던거 pop
            stack.append(wordList[i])   #새로운거 다시 스택에 넣기
        #스택에 있는 꼭대기랑, 현재 비교한 값이랑 같은 경우 False
        else :
            return False
    return True


while True :
    word = input()
    if word == "end" :
        break
    
    #1. 모음(a,e,i,o,u) 하나를 반드시 포함
    if checkEssential(word) :
        if checkRecurWord(word) : 
            if checkSameWord(word) :
                print(f'<{word}> is acceptable.')
            else :
                print(f'<{word}> is not acceptable.')
        else :
            print(f'<{word}> is not acceptable.')
    else :
        print(f'<{word}> is not acceptable.')