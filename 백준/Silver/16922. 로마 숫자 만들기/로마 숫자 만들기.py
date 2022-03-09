from itertools import combinations_with_replacement

n = int(input())
num_list = [1, 5, 10, 50]
result = []
#중복조합 리스트 : combinations_with_replacement([반복가능한 개체], 길이)
#[1, 5, 10, 50]에 있는 숫자를 n개 뽑는다(중복 가능)
com_list = list(combinations_with_replacement(num_list, n))

#중복조합으로 n개 뽑은 종류 리스트를 더해준다.
for i in com_list :
    result.append(sum(i))

print(len(set(result)))     #더한 값이 중복값일 수 있어서 set이용