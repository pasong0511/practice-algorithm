import sys

T = int(sys.stdin.readline())
for i in range(T) :
    num = int(sys.stdin.readline())
    count = 0
    i = 5

    # 5가 몇개가 들어가는지 구해준다.
    while i <= num :
        count += num // i   #5의 배수의 합을 구한다.
        i *= 5
    
    print(count)