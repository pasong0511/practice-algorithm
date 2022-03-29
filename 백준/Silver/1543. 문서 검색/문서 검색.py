import re

input_string = input()
find_string = input()
regex = re.compile(f'({find_string})')      #괄호 넣어줘야 하므로 f스트링으로 () 추가

re_result = regex.findall(input_string)
print(len(re_result))
