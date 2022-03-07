import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    num_list.append([x, y])

new_list = sorted(num_list, key = lambda x : (x[1], x[0]))

for i in range(n) :
    print(new_list[i][0], new_list[i][1])