import math

n, m = map(int, input().split())
students = [[0] * 7 for _ in range(2)]		#i:[0] 성별 / j:[1] 학년 

for i in range(n) :
	s, c = map(int, input().split())        
	students[s][c] += 1                     #이차원 리스트에 성별과 학년에 맞게 누적

room = 0
for student in students :
	for single in student :
		room += math.ceil(single / m)					#m으로 나눠서 나누어 떨어지지 않은 경우, 방 인원보다 넘었음 -> 올림 처리
		
print(room)