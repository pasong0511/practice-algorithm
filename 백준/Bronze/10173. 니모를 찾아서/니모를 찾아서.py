import re

while True :
    input_string = input()
    if input_string == "EOI" :
        break
    regex = re.findall("([nN][eE][mM][oO])", input_string);
    if len(regex) >= 1 :
        print("Found")
    else :
        print("Missing")