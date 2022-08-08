def dac(a, b) :

    #b가 1인 경우 곱할필요 없어, 나머지 리턴
    if b == 1 :
        return a % c

    #dac 함수를 통해 a를 (b//2)번 곱한 나머지를 구함.
    temp = dac(a, (b // 2))

    #b가 짝수인 경우
    if b % 2 == 0 :
        #temp를 제곱으로 나눈 나머지를 리턴
        return temp * temp % c
    #b가 짝수인 경우
    else :
        #temp 제곱 후 a를 한번 더 곱한 후 C를 나눠야 a를 b번 곱한 후 C로 나눈 나머지가 구해짐.
        return temp * temp * a % c


A, B, c = map(int, input().split())

print(dac(A, B))


#A를 B번 곱한다
#숫자가 매우 커질수있으므로 C로 나눈다.