import sys
input = sys.stdin.readline

n = int(input())
data_list = list(map(int, input().split()))
data_list.insert(0, 0)          #1부터 시작하기 위해서 맨 앞에 0 삽입
result_num = []
dy = [0] * (n + 1)
dy[1] = 1                       #인덱스 1에는 앞에 붙일 숫자 없음


def solutuon(n) :
    result_max = 0
    

    if n == 1 :
        print(1)
        print(data_list[1])
        return

    for i in range(2, n+1) :
        max_len = 0

        #i-1부터 0까지 data_list[i]값 보다 작으면서 최대 길이가 긴 경우
        #그 긴 길이에 +1 해서 증가 수열을 구함
        for j in range(i-1, 0, -1):
            if data_list[j] < data_list[i] and dy[j] > max_len :        #[i]보다 [j]는 무조건 작은 수
                max_len = dy[j]                                         #최대 길이값 찾음
        dy[i] = max_len + 1                                             #i-1번째부터 최대 길이 찾은 값으로부터 +1 한다

        
        #만들어둔 dy값을 이용해서 제일 긴 증가수열 찾음
        if dy[i] > result_max : 
            result_max = dy[i]
    
    order = result_max              #dy의 최대 길이 저장

    for i in range(n, 0, -1) :      #dy리스트를 -1하면서 <--- 방향으로 찾음
        if dy[i] == order :         #최대 길이를 찾았늘때
            result_num.append(data_list[i])         #그 인덱스가 최대 길이 만든 값
            order -= 1              #-1해줘서 다음 작은 최대 길이 찾기
    
    result_num.reverse()    

    print(result_max)
    print(" ".join(map(str, result_num)))

solutuon(n)
