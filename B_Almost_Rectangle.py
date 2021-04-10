for _ in range(int(input())):
    n = int(input())

    g = []
    for i in range(n):
        g.append(list(input()))
    one, two = [], []
    for i in range(n):
        for j in range(n):
            if len(one) == 0 and g[i][j] == '*':
                one = [i, j]
            elif g[i][j] == '*':
                two = [i, j]

    if one[1] == two[1]:
        dist = abs(one[0] - two[0])
        if one[1] - 1 >= 0:
            y = one[1] - 1
        else:
            y = one[1] + 1
        three = [one[0], y]
        four = [two[0], y]
    elif one[0] == two[0]:
        #dist = abs(one[1] - two[1])
        if one[0] - 1 >= 0:
            x = one[0] - 1
        else:
            x = one[0] + 1
        three = [x, one[1]]
        four = [x, two[1]]
    elif one[0] < two[0] and one[1] < two[1]:
        three = [two[0], one[1]]
        four = [one[0], two[1]]
    else:
        three = [one[0], two[1]]
        four = [two[0], one[1]]
    #print(three, four)
    for i in range(n):
        for j in range(n):
            if [i, j] == three or [i, j] == four:
                g[i][j] = '*'

    for i in g:
        print("".join(i))
    # print()
