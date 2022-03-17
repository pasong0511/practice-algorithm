n = int(input())
road_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

cost = 0
min_cost = 2147000000

for i in range(n-1) : 
    if oil_price[i] <= min_cost :                    #최소값 갱신하면서 기름 넣어주기
        cost += oil_price[i] * road_length[i]       #비용 += 오일 가격 * 거리
        min_cost = oil_price[i]                     #최소값 갱신
        continue
    if oil_price[i] > min_cost :                    #최소값보다 오일 가격비 이비싸면 
        cost += min_cost * road_length[i]           #최소값으로 거리 곱해줌

print(cost)