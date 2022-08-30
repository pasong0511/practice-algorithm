import sys

line = sys.stdin.readline()
answer = ''

stack = []
wordStack = []
idx = 0

for i in range(len(line)) :
  if line[i] == "<" :
    stack.append(line[i])

    if 0 < len(wordStack) : 
      
      #print("출력1", "".join(wordStack))
      transeWod = "".join(wordStack)[::-1]
      #print("반전1", transeWod)
      answer += transeWod
      wordStack = []

    continue

  if line[i] == ">" :
    stack.append(line[i])
    
    #print("".join(stack))
    answer += "".join(stack)
    stack = []
    continue

  if len(stack) > 0 :
    stack.append(line[i])
    continue

  if len(wordStack) > 0 :

    #인덱스 끝인 경우
    if i == len(line) - 1 : 
      wordStack.append(line[i])     #공백도 추가하고 스택에 넣기
      
      #print("출력2", "".join(wordStack))

      transeWod = "".join(wordStack)[::-1]
      #print("반전2", transeWod)
      answer += transeWod
      wordStack = []
      continue

    #공백인 경우
    if line[i] == " " : 
      #print("출력3", "".join(wordStack))

      transeWod = "".join(wordStack)[::-1]
      transeWod += ' '              #공백은 뒤에 추가
      #print("반전3", transeWod)
      answer += transeWod
      wordStack = []
      continue

  if len(stack) == 0 :
    wordStack.append(line[i])

  #print(wordStack)

print(answer.replace("\n", ""));