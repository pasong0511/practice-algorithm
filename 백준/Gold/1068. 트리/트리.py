import sys

n = int(input())
parentNode = list(map(int, input().split()))
delNode = int(input())

def DFS(d) :
    #지울 부모노드 -2로 변경하기
    parentNode[d] = -2
    
    #반복문 돌면서 parentNode노드에 지운 부모노드를 바라보고있는 자식노드 -2로 변경해주기
    #i가 자식노드가 바라보는 부모노드임
    for i in range(n) :
        #parentNode[i]-> 여기서는 자식 노드 번호임
        #부모노드가 i를 갖는 사직 노드를 -2 처리해줘야함
        if d == parentNode[i] :     #i가 부모노드
            DFS(i)

DFS(delNode)
count = 0
for i in range(n) :
    if parentNode[i] != -2 and i not in parentNode :
        count += 1
print(count)