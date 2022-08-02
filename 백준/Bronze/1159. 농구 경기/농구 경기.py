n = int(input())
first_dic = {}
result_list = []

#앞글자만 딴 딕셔너리 생성 초기값은 1, 확인될때마다 누적
for i in range(n) :
    name = list(input())
    if name[0] not in first_dic :
        first_dic[name[0]] = 1
    else :
        first_dic[name[0]] += 1

#개수가 5 이상인 성 찾기
for key, values in first_dic.items() :
    if values >= 5 :
        result_list.append(key)

result_list.sort()
#성이 5개 이상이 있는 경우 정답 출력, 아니면 기권
if len(result_list) > 0 :
    print("".join(result_list))
else :
    print("PREDAJA")

#성의 첫글자가 같은 선수 5명선발
#뽑을 수 있는 성의 첫번째 글자 뽑기

#성의 첫글자가 5명 이하인 경우 기권
#->"PREDAJA"

#첫글자만 뽑아서 누적하는 딕셔너리 생성
#item이 5 이상인 경우 출력
#item이 5 이상인게 없는 경우 출력하지 기권 출력