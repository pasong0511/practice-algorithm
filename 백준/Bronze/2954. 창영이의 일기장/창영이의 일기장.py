import re

string_list = input()
regex = re.compile("(a|e|i|o|u)p(a|e|i|o|u)");
print(re.sub(regex, "\\1", string_list))
