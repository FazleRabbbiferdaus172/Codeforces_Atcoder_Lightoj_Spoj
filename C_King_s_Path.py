x0, y0, x1, y1 = map(int, input().split())
n = int(input())
g = set()
for _ in range(n):
    a, b, c = map(int, input().split())
    for i in range(b, c+1):
        g.add((a, i))

moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
# print(g)
q = [(x0, y0, 0)]
g.remove((x0, y0))
ans = -1
while q:
    # print(len(q))
    temp = q.pop(0)
    # print(temp)
    if temp[:2] == (x1, y1):
        ans = max(ans, temp[2])

    for move in moves:
        temp_move = (temp[0] + move[0], temp[1] + move[1], temp[2] + 1)

        if len(g) == 0 or not temp_move[:2] in g:
            continue
        q += [temp_move]
        g.remove(temp_move[:2])
        #print("TEST", temp_move, g[temp_move[0]])

print(ans)
