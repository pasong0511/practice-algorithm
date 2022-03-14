n = int(input())
time_list = []

for i in range(n) :
    start, end = map(int, input().split())
    time_list.append([start, end])

time_list.sort(key=lambda x : (x[1], x[0])) #끝나는 시간으로 오름차순 정렬

end_time = 0                                #다음 시작 시간을 찾기 위해 끝나는 시간 저장
count = 0

for start_plan, end_plan in time_list :
    if start_plan >= end_time :             #시작 시간이 끝나는 시간보다 크거나 같은경우
        end_time = end_plan                 #시작 시간의 끝이 다음 끝나는 시간이 된다 
        count += 1

print(count)