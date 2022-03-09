a = -1
b = -1

while a != 0 and b != 0 :
    a, b = map(int, input().split())
    count = 0

    if a != 0 and b != 0 :
        if a % b == 0 :         #소수 판별
            print("multiple")
        elif b % a == 0 :         #배수 판별
            print("factor")
        else :
            print("neither")