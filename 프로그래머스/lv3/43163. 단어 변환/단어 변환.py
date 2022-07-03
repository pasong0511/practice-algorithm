def solution(begin, target, words):
    answer = 0
    
    #타겟이 words에 없는 경우 0 반환
    if target not in words :
        return 0
    
    return answer

#두개의 단어, begin, target
#begin에서 target으로 변환하는 가장 짧은 변환 과정
#한번에 한개의 알파벳 바꿈
#words에 있는 단어로 만 변경