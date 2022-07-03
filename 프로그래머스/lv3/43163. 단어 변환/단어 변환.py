result = []

def differWordCount(begin, word) :
    differ = 0 
    for i in range(len(begin)) :
        if begin[i] != word[i] :
            differ += 1
    return differ

def DFS(begin, target, words, visited, L) :
    #종료조건 : begin과 target이 같은 경우 종료
    if begin == target :
        result.append(L)
        return
    
    #반복문 돌면서 begin과 words에 있는 words[i]가 차이가 1인 경우를 찾는다
    # 찾은 경우 그 words[i]가 다음 begin
    # 반복 방문을 하지 않기 위해 visited False처리
    # 이미 방문한 곳은 재방문 하지 않기 visited is True
    for i in range(len(words)) :
        #방문한 단어는 재방문 하지 않는다.
        if visited[i] is True :
            continue
        
        #begin과 words[i]를 비교해서 차이가 1인 경우 찾기
        if differWordCount(begin, words[i]) == 1 :
            visited[i] = True
            DFS(words[i], target, words, visited, L+1)
            visited[i] = False

    

def solution(begin, target, words):
    global result
    #words에 있는 단어를 하나씩 뽑아서 begin과 비교할 건데, 방문했던거 또 방문할 수 없으니까 방문처리용 만들어줌
    visited = [0 for _ in range(len(words))]
    
    #종료조건 : target이 words에 없는 경우 종료
    if target not in words :
        return 0
    
    DFS(begin, target, words, visited, 0)
    return min(result)
    

#두개의 단어, begin, target
#begin에서 target으로 변환하는 가장 짧은 변환 과정
#한번에 한개의 알파벳 바꿈
#words에 있는 단어로 만 변경