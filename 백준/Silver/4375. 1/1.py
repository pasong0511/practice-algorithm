def one(num) :
    temp = '1'

    while True :
        if int(temp) % num == 0 :
            return len(temp)
        temp += '1'                   #1 추가

while True :
    try :
        num = int(input())
        print(one(num))
    except EOFError:
        break