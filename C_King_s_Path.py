x0, y0, x1, y1 = map(int, input().split())
n = int(input())
g = {}
for _ in range(n):
    a, b, c = map(int, input().split())
    if a not in g:
        g[a] = []

    g[a] += [i for i in range(b, c+1)]
    g[a] = set(g[a])
    g[a] = list(g[a])

moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, -1), (-1, 1)]

q = [(x0, y0, 0)]
visited = [(x0, y0)]
ans = -1
while q:
    # print(len(q))
    temp = q.pop(0)
    if temp[:2] == (x1, y1):
        ans = max(ans, temp[2])

    for move in moves:
        temp_move = (temp[0] + move[0], temp[1] + move[1], temp[2] + 1)
        if temp_move[0] in g and temp_move[1] in g[temp_move[0]] and not temp_move[:2] in visited:
            q += [temp_move]
            visited += [temp_move[0:2]]

print(ans)
