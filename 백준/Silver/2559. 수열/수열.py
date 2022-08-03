n, k = map(int, input().split())
num_list = list(map(int, input().split()))
max_list = []

part_sum = sum(num_list[:k])       #초기 부분 수열 구하기
max_list.append(part_sum)          #리스트에 저장하기

for i in range(len(num_list)-k) :
    part_sum = (part_sum - num_list[i]) + num_list[i+k]
    max_list.append(part_sum)

print(max(max_list))