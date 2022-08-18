import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
result = [-1] * n

for i in range(n) :
    while stack :
        if num_list[i] > num_list[stack[-1]] :      #현재 비교대상 값(num_list[i])과 스택의 꼭대기에 인덱스의 값과 비교
            result[stack.pop()] = num_list[i]
        else :
            break
    stack.append(i)

print(*result)