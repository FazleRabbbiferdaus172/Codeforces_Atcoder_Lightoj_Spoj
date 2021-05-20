def dfs(x, y, j):
    global v, g, move_x, move_y
    if j > 10:
        return
    if v[x][y][j] == 1:
        return
    v[x][y][j] = 1

    for i in range(4):
        temp_x, temp_y, temp_j = x + move_x[i], y + move_y[i], j
        if g[temp_x][temp_y] == '#':
            continue
        if g[temp_x][temp_y] == 's':
            temp_j += 1
        dfs(temp_x, temp_y, temp_j)


n, m, cap = map(int, input().split())
g = ['#'*(m+2)]
for _ in range(n):
    g += ['#' + input()+'#']
g += ['#'*(m+2)]
# print(g)

move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]

v = [[[0]*11 for i in range(m+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if g[i][j] == 'x':
            # print("ok")
            dfs(i, j, 0)
            break

ans = "IMPOSSIBLE"
for i in range(1, n+1):
    for j in range(1, m+1):
        if g[i][j] == '@':
            # print(v[i][j])
            for count in range(cap//2+1):
                if v[i][j][count] == 1:
                    ans = "SUCCESS"
                    break
'''
for i in v:
    print(i)'''
print(ans)
