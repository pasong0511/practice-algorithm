n = int(input())
data_list = list(map(int, input().split()))
data_list.insert(0, 0)          #1부터 시작하기 위해서 맨 앞에 0 삽입
dy = [0] * (n + 1)
dy[1] = 1                       #인덱스 1에는 앞에 붙일 숫자 없음


def solutuon(n) :
    result_max = 0

    if n == 1 :
        return 1

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
    return result_max 

print(solutuon(n))
