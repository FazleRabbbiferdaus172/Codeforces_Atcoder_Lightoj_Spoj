
def wins(s):
    global g
    count = 0
    if g[0] == s*3:
        count += 1
        # print(1)
    if g[1] == s*3:
        count += 1
        # print(2)
    if g[2] == s*3:
        count += 1
        # print(3)
    if g[0][0] == s and g[1][0] == s and g[2][0] == s:
        count += 1
        # print(4)
    if g[0][1] == s and g[1][1] == s and g[2][1] == s:
        count += 1
        # print(5)
    if g[0][2] == s and g[1][2] == s and g[2][2] == s:
        count += 1
        # print(6)
    if g[0][0] == s and g[1][1] == s and g[2][2] == s:
        count += 1
        # print(7)
    if g[0][2] == s and g[1][1] == s and g[2][0] == s:
        count += 1
        # print(8)

    return count


T = int(input())

for t in range(T):
    x, o = 0, 0
    g = []
    for _ in range(4):
        try:
            xx = input().strip()
            g.append(xx)
        except EOFError as error:
            xx = ""
        x += xx.count('X')
        o += xx.count('O')

    # print("*****************")
    wins_x, wins_o = wins('X'), wins('O')
    if x - o > 1 or x - o < 0:
        print("no")
    elif wins_x > 0 and x - o != 1:
        print("no")
    elif wins_o > 0 and x - o != 0:
        print("no")
    elif wins_o > 0 and wins_x > 0:
        print("no")
    else:
        print("yes")
    # print("******************")
