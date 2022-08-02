n = int(input())
star = input().split("*")           #*를 기준으로 앞 뒤 자르기
star_left = star[0]                 #* 기준 앞
star_right = star[1]                #* 기준 뒤

for i in range(n) :
    name = input()
    
    if star_left == name[:len(star_left)] and star_right == name[-len(star_right):] and len("".join(star)) <= len(name):
        #입력한 폴더의 길이가 잘라서 만든 길이보다 더 길어야함
        print("DA")
    else :
        print("NE")