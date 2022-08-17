import sys
input = sys.stdin.readline

dic = {}
n = 0

while True:
    tree = input().rstrip()
    if not tree : 
        break

    if tree not in dic :
        dic[tree] = 1
    else :
        dic[tree] += 1
    n += 1

sordDic = sorted(list(dic))

for tree in sordDic :
    print(f'{tree} {(dic[tree] / n * 100):.4f}')