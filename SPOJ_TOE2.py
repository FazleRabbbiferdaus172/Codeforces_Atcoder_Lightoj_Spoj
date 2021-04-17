
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


while True:

    xx = input()
    if xx == "end":
        break
    x, o = xx.count('X'), xx.count('O')
    g = []
    g.append(xx[:3])
    g.append(xx[3:6])
    g.append(xx[6:])
    wins_x, wins_o = wins('X'), wins('O')
    # print(g)
    #print(x, o)
    #print(wins_x, wins_o)
    if x - o > 1 or x - o < 0:
        print("invalid")
    elif wins_x > 0 and x - o != 1:
        print("invalid")
    elif wins_o > 0 and x - o != 0:
        print("invalid")
    elif wins_o > 0 and wins_x > 0:
        print("invalid")
    elif wins_o == 0 and wins_x == 0 and x+o != 9:
        print("invalid")
    else:
        print("valid")
