import sys
from collections import deque

#push X: 정수 X를 큐에 넣는 연산이다.
def queue_push(queue, num):
    queue.append(num);

#pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def queue_pop(queue) :
    if queue_empty(queue) == 0 :       #큐가 비어있지 않아서 뺄수 있는 경우
        return queue.popleft()         #만 앞에서 숫자 뺌
    if queue_empty(queue) == 1 :
        return -1

#size: 큐에 들어있는 정수의 개수를 출력한다.
def queue_size(queue) :
    return len(queue)

#empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
def queue_empty(queue) :
    if len(queue) > 0 :              #차 있는 경우 0 반환
        return 0
    if len(queue) == 0 :            #비어있는 경우 1 반환
        return 1

#front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def queue_front(queue) :
    if queue_empty(queue) == 0 :
        return queue[0]
    if queue_empty(queue) == 1 :
        return -1

#back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def queue_back(queue) :
    if queue_empty(queue) == 0 :
        return queue[-1]
    if queue_empty(queue) == 1 :
        return -1

def solution() :
    queue = deque()
    n = int(sys.stdin.readline())

    for i in range(n) :
        line = list(map(str, sys.stdin.readline().rstrip().split()))
        if line[0] == "push" :
            queue_push(queue, line[1])
            continue
        if line[0] == "pop" :
            print(queue_pop(queue))
            continue
        if line[0] == "size" :
            print(queue_size(queue))
            continue
        if line[0] == "empty" :
            print(queue_empty(queue))
            continue
        if line[0] == "front" :
            print(queue_front(queue))
            continue
        if line[0] == "back" :
            print(queue_back(queue))
            continue

solution()