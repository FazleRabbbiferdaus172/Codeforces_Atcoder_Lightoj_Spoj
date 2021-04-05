n, m = map(int, input().split())
l = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x, y))
dbl = []
ans = 0
for i in range(n):
    ans += min(l[i])
    if l[i][1] > l[i][0]:
        dbl += [i]

xx = sorted([min(l[i][0]*2, l[i][1]) - min(l[i][0], l[i][1])
             for i in dbl], reverse=True)


for i in range(min(m, len(xx))):
    ans += xx[i]

print(ans)
