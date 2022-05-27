h, r = map(int, input().split())

board = []
for i in range(h):
    temp = input()
    t = []
    for j in temp:
        t.append(j)
    board.append(t)

rot_board = list(map(list, zip(*board)))

word_list = []
for word in board:
    cut = "".join(word)
    cut_li = cut.split("#")
    for i in cut_li:
        if i != "" and len(i) > 1:
            word_list.append(i)

for word in rot_board:
    cut = "".join(word)
    cut_li = cut.split("#")
    for i in cut_li:
        if i != "" and len(i) > 1:
            word_list.append(i)

word_list.sort()
print(word_list[0])