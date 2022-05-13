n, s = map(int, input().split())
numbers = list(map(int, input().split()))


def dfs(i, sum):
    global res
    if i == n:                     #i가 n까지 다 돌았으면 종료 
        return
    if sum + numbers[i] == s:      #합이 s이면 카운트 증가     
        res += 1

    dfs(i + 1, sum)
    dfs(i + 1, sum + numbers[i])


res = 0
dfs(0, 0)
print(res)