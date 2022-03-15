from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
permu_list = list(permutations(num_list))   #모든 순열 리스트 만들기

max_value = -1

for permu in permu_list :                    #모든 순열 리스트에 있는거 하나씩 뽑아오기
    sum_num = 0
    for i in range(n-1) :
        num = abs(permu[i+1] - permu[i])
        sum_num += num
    if sum_num > max_value :                #차의 합 중 최대 합을 찾기
        max_value = sum_num

print(max_value)
