minus_split = list(input().split("-"))                       #- 기호로 자르게
cal_num_list = []

for none_minus in minus_split :
    plus_split = none_minus.split("+")                      #-로 자른 숫자를 +로 또 자르기
    
    plus_sum = 0
    for i in plus_split :                                   #+로 자른 값은 합해서 값을 키워준다
        plus_sum += int(i)
    cal_num_list.append(plus_sum)

result = cal_num_list[0]                                    #첫번째 값은 그대로
for i in range(1, len(cal_num_list)) :                      #합으로 만들어준 값을 -값으로 빼주면 최소값 나옴
    result -= cal_num_list[i]

print(result)