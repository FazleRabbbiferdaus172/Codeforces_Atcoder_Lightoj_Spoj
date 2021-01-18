l = []
for i in range(5):
    l.append(list(map(int, input().split())))
mx = -1
s = set()
for a in range(5):
    for b in range(5):
        for c in range(5):
            for d in range(5):
                for e in range(5):
                    if len(set([a, b, c, d, e])) == 5:
                        x = l[a][b] + l[b][a] + l[c][d] + l[d][c] + l[b][c] + l[c][b] + \
                            l[d][e] + l[e][d] + l[c][d] + \
                            l[d][c] + l[d][e] + l[e][d]
                        mx = max(mx, x)

print(mx)
