test_case = int(input())

for case in range(test_case) :
    price_n = int(input())
    num_list = list(map(int, input().split()))

    result = []

    while num_list :
        now_value = num_list.pop(0)
        if (now_value * 100 // 75) in num_list :
            result.append(now_value)
            num_list.remove((now_value * 100 // 75))

    print(f'Case #{case+1}: {" ".join(map(str, result))}')