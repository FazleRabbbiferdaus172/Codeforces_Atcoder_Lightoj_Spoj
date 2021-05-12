for t in range(int(input())):
    n, m = map(int, input().split())
    g = []
    for _ in range(n):
        g.append(list(map(int, input().split())))
    new_g = [[-1]*m for _ in range(n)]
    q = []
    ans = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m-1:
                new_g[i][j] = g[i][j]
                q += [(g[i][j], i, j)]
    '''for i in new_g:
        print(i)'''
    move_x = [0, 0, 1, -1]
    move_y = [1, -1, 0, 0]
    while q:
        temp = min(q)
        q.remove(temp)
        llq = len(q)
        for i in range(4):
            x, y = temp[1] + move_x[i], temp[2] + move_y[i]
            if x >= n or y >= m or x < 0 or y < 0:
                continue
            if new_g[x][y] != -1:
                continue
            new_g[x][y] = max(temp[0], g[x][y])
            ans += new_g[x][y] - g[x][y]
            q.append((new_g[x][y], x, y))
    print(ans)
    try:
        input()
    except:
        continue
