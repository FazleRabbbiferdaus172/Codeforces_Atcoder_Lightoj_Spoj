
def iswin(g):
    row = (g[0] != '.' and g[0] == g[1] and g[1] == g[2]) or (g[3] != '.' and g[3]
                                                              == g[4] and g[4] == g[5]) or (g[6] != '.' and g[6] == g[7] and g[7] == g[8])
    col = (g[0] != '.' and g[0] == g[3] and g[3] == g[6]) or (g[1] != '.' and g[1]
                                                              == g[4] and g[4] == g[7]) or (g[2] != '.' and g[2] == g[5] and g[5] == g[8])
    digon = (g[0] != '.' and g[0] == g[4] and g[4] == g[8]) or (
        g[2] != '.' and g[2] == g[4] and g[4] == g[6])

    return row or col or digon


for _ in range(int(input())):
    x, o = 0, 0
    g = []
    for _ in range(4):
        try:
            g += list(input().strip())
        except EOFError as error:
            continue

    init = ['.']*9
    que = [(init, 0)]
    ans = "no"
    while len(que):
        cur = que[0][0]
        cur_p = que[0][1]
        que.pop(0)
        if cur == g:
            ans = "yes"
            break

        if iswin(cur):
            continue

        for i in range(9):
            if cur[i] == '.':
                cur[i] = ['X', 'O'][cur_p]
                if cur[i] == g[i]:
                    xx = cur[:]
                    que.append((xx, 1 ^ cur_p))
                cur[i] = "."

    print(ans)
