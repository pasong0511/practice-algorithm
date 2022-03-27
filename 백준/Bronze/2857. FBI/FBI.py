import re

index = 0
result = []
while True :
    try :
        index += 1
        input_text = input() 
        regex = re.compile("[A-Z0-9\-]*FBI[A-Z0-9\-]*")
        re_text = regex.findall(input_text)
        
        if len(re_text) != 0 :
            result.append(index)
    except :
        break
if len(result) != 0 :
    for i in result :
        print(i)
else : 
    print("HE GOT AWAY!")