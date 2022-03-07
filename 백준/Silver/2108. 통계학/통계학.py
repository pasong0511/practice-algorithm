import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []

for i in range(n) :
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

print(round(sum(num_list) / n))                     #산술평균
print(num_list[n//2])                               #중앙값

many_value = sorted(Counter(num_list).most_common(), key = lambda x : (-x[1], x[0]))    #최빈값
if n == 1 :                                         #n이 한개이면 num_list[0]이 최빈값
    print(num_list[0])
else :
    if many_value[0][1] != many_value[1][1] :       #정렬된 개수 센거랑 비교, 같지 않은 경우
        print(many_value[0][0])                     #그냥 0번째가 제일 많이 나옴
    else :
        print(many_value[1][0])                     #0번째랑, 1번째랑 같은 빈도수이기 때문에 1번 출력

print(num_list[-1] - num_list[0])                   #범위


#N은 홀수
#산술평균 : N개의 수들의 합을 N으로 나눈 값
#중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
#최빈값 : N개의 수들 중 가장 많이 나타나는 값
#범위 : N개의 수들 중 최댓값과 최솟값의 차이