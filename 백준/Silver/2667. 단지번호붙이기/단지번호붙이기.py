import sys
from collections import deque

def DFS(current_x, current_y, map_data) :
    global count
    global n
    
    dx = [-1, 0, 1, 0]      #top, right, bottom, light
    dy = [0, 1, 0, -1]

    count += 1

    map_data[current_x][current_y] = 0

    for i in range(4) :
        next_x = current_x + dx[i]
        next_y = current_y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n and map_data[next_x][next_y] == 1:
            DFS(next_x, next_y, map_data)

def solution() :
    global n
    global count

    n = int(input())
    maps = []
    result = []

    for i in range(n) :         #map 입력 받기
        m = input()
        temp = []
        for j in m :
            temp.append(int(j)) 
        maps.append(temp)
    
    for i in range(n) :
        for j in range(n) :
            if maps[i][j] == 1 :
                
                count = 0
                DFS(i, j, maps)
                result.append(count)
    print(len(result))
    result.sort()
    for i in result :
        print(i)

solution()