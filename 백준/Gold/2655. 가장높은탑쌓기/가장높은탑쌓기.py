N = int(input())
mapp = []
mapp.append((1,1,1,1))
for i in range(1,N+1):
    a,b,c = map(int, input().split()) #(넓이, 높이, 무게) 순서
    mapp.append((i,a,b,c))
 
#dp
dp = [0]*(N+1)
#무게 순으로 일단 정렬
mapp.sort(key = lambda x: x[3])
 
#mapp를 훑으면서 dp를 갱신
for i in range(1,N+1):
    for j in range(0,i):
        if mapp[i][1]>mapp[j][1]: #현재 넓이가 훑으며 거쳐온 이전 넓이보다 클 때
            dp[i] = max(dp[i], dp[j]+mapp[i][2])
            
#가장 높이 쌓을 수 있는 높이 찾기
max_height = max(dp)
 
#기억을 더듬으며 백 트래킹
index = N
history = []
 
while index!=0:
    if dp[index]==max_height:
        history.append(mapp[index][0])
        max_height-=mapp[index][2]
    index-=1
    
print(len(history))
history.reverse()
for i in history:
    print(i)