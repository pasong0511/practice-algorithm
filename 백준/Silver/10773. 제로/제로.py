n = int(input())
num_list = []

for i in range(n) :
    num = int(input())
    if num != 0 :
        num_list.append(num)
        continue
    if num == 0 :
        if len(num_list) > 0 :
            num_list.pop()

print(sum(num_list))