borad = [0] * 101                                   #시간에 따른 트럭 개수 저장
accumulate = 0

charge_list = list(map(int, input().split()))       #요금 저장

for i in range(3) :
    start, end = map(int, input().split())
    for time in range(start, end) :
    #시작 시간 끝 시간으로 board에 누적해서 그 시간에 트럭이 몇개 있는지 체크
        borad[time] += 1

for i in range(len(borad)) :
    if borad[i] == 1 :
        accumulate += (borad[i] * charge_list[0])  #1대가 있으면 charge_list[0]
    elif borad[i] == 2 :
        accumulate += (borad[i] * charge_list[1])  #2대 있으면 charge_list[1]
    elif borad[i] == 3 :
        accumulate += (borad[i] * charge_list[2])  #3대 있으면 charge_list[2]

print(accumulate)