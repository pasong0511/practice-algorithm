import re

while True :
    input_text = input()
    if input_text == "#" :
        break
    regex = re.compile("[AaEeIiOoUu]")
    re_text = regex.findall(input_text)
    print(len(re_text))