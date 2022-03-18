n = int(input())
sum = 0
count = 0
total = 0

while True :
    if n < total :
        break
    else :
        count += 1
        total += count
print(count-1)