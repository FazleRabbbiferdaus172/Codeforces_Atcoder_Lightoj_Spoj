n = int(input())
d = {}

for i in range(n):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = [1, 0]
    else:
        d[a][0] += 1
    if b != a:
        if not b in d:
            d[b] = [1, 1]
        elif d[b][1] == 0:
            d[b][1] = 1
    else:
        d[b] = [1, 0]
ans = 0
for i in d:
    if d[i][1] == 0:
        ans += d[i][0]
print(d)
print(ans)
