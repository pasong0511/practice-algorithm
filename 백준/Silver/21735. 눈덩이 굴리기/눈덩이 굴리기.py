n, minutes = map(int, input().split())             #앞마당 길이 n, 대회사긴 minutes
num_list = [0] + list(map(int, input().split()))
max = -1

def DFS(index, size, time) :
    global max

    #시간이 m 초과하면 종료
    if time > minutes :           
        return
    #시간을 초과하지 않으면 눈덩이 크기 비교해서 최대값 갱신
    if time <= minutes :          
        if size > max :
            max = size

    #눈덩이 굴리기(a[i] + 1)
    if index <= n-1 :
        #다음 인덱스+1, 키운 사이즈, 시간+1
        DFS(index+1, size+num_list[index+1], time+1)
    
    #눈덩이 던지기 : (원래 크기 // 2) + (a[i]+2)
    if index <= n-2 :
        #다음 인덱스+2, 키운 사이즈, 시간+1
        DFS(index+2, (size//2) + num_list[index+2], time+1)

DFS(0, 1, 0)        #눈덩이의 시작 위치는 0, 시작크기는 1, 시작 시간은 0
print(max)