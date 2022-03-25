import sys
from collections import deque

num = int(input())
for _ in range(num):
    n, pick_index = map(int, input().split())
    num_list = list(map(int,input().split()))
    queue = deque(num_list)

    cnt = 0
    while queue:
        top = max(queue)
        pick_index -= 1
        pop = queue.popleft()
        if top != pop:                  #pop한게 top과 다르면 뒤로 붙여줌
            queue.append(pop)

            if pick_index < 0:          #찾아야할 인덱스가 0보다 작아지면 뒤로 보낸 인덱스로 변경           
                pick_index = len(queue)-1
        else:                           #pop한게 top과 같으면
            cnt+=1                      #카운트 층가
            if pick_index == -1:        #찾아야할 인덱스가 우선순위 차례가 되서 나올 순서가 되는 겨우
                print(cnt)
                break                   #반복문 중단