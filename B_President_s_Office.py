n, m, c = map(str, input().split())
n, m = int(n), int(m)
g = [[] for i in range(n)]
for i in range(n):
    x = list(input())
    g[i] = x

s = set()

for i in range(n):
    for j in range(m):
        u = i-1
        d = i+1
        r = j+1
        l = j-1
        if g[i][j] == c:
            if u >= 0 and g[u][j] != '.' and g[u][j] != c:
                s.add(g[u][j])
            if d < n and g[d][j] != '.' and g[d][j] != c:
                s.add(g[d][j])
            if r < m and g[i][r] != '.' and g[i][r] != c:
                s.add(g[i][r])
            if l >= 0 and g[i][l] != '.' and g[i][l] != c:
                s.add(g[i][l])
print(len(s))
