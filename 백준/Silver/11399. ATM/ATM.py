n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()
result = 0

for i in range(n) :
    result += sum(num_list[:i+1])

print(result)