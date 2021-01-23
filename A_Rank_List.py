n, k = map(int, input().split())

tm = []

for _ in range(n):
    p, t = map(int, input().split())
    tm.append([p, t])

tm.sort(key=lambda x: (x[0] * -1, x[1]))
ans = tm.count(tm[k-1])
print(ans)
