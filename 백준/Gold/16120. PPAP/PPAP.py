word = input()
stack = []
ppap = ['P', 'P', 'A', 'P']

for w in word :
    stack.append(w)                     #무조건 하나씩 스택에 넣는다.
    if len(stack) >= 4 : 
        if stack[-4:] == ppap :
            stack.pop()
            stack.pop()
            stack.pop()

if stack == ppap or stack == ["P"] :
    print("PPAP")
else :
    print("NP")