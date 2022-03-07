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
    if many_value[0][1] != many_value[1][1] :       #개수 센
        print(many_value[0][0])
    else :
        print(many_value[1][0])

print(num_list[-1] - num_list[0])                   #범위