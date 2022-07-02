count = 0

def DFS(numbers, target, index, score) :
    global count
    
    #인덱스가 배열의 길이만큼 다 만든 경우 종료
    if index == len(numbers) :
        #만든 점수가 타켓과 같은 경우 만들수있는 경우의 수 증가 +1
        if score == target :
            count += 1
            return 
    else :
        DFS(numbers, target, index+1, score + numbers[index])
        DFS(numbers, target, index+1, score - numbers[index])
    
def solution(numbers, target):
    DFS(numbers, target, 0, 0)
    return count



#n개의 음이 아닌 정수
#정수들을 순서를 바꾸지 않고, 적절히 빼거나, 더해서 타겟 넘버 만듬
#인덱스의 숫자 한개씩 뽑아가면서 +, -의 경우의 수를 만든다
#예시에 보여줄 숫자 나열은 필요가 없다 -> 경우의 수의 개수만 만들면 되니까
#socre를 사용하여, 더하거나 빼는 것을 누적해서 DFS로 전달한다.
#+를 사용한다
#-를 사용한다
