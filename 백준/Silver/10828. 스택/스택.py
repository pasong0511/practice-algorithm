import sys

#push X: 정수 X를 스택에 넣는 연산이다.
def stack_push(stack, num):
    stack.append(num);

#pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def stack_pop(stack) :
    if stack_empty(stack) == 1 :        #비어있는 경우 1, pop 불가능 -1 출력
        return -1
    return stack.pop()                  #비어있지 않는 경우, pop 가능

#size: 스택에 들어있는 정수의 개수를 출력한다.
def stack_size(stack) :
    return len(stack)

#empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
def stack_empty(stack) :
    if len(stack) > 0 :         #차 있는 경우 0 반환
        return 0
    if len(stack) == 0:         #비어있는 경우 1반환
        return 1

#top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def stack_top(stack) :
    if stack_empty(stack) == 1 :        #비어있는 경우 1, pop 불가능 -1 출력
        return -1
    return stack[-1]

def solution() :
    stack = []
    n = int(sys.stdin.readline())
    order = []

    for i in range(n) :
        line = list(map(str, sys.stdin.readline().rstrip().split()))
        order.append(line)
        if line[0] == "push" :
            stack_push(stack, int(line[1]))
            continue
        if line[0] == "pop" :
            print(stack_pop(stack))
            continue
        if line[0] == "size" :
            print(stack_size(stack))
            continue
        if line[0] == "empty" :
            print(stack_empty(stack))
            continue
        if line[0] == "top" :
            print(stack_top(stack))
            continue

solution()