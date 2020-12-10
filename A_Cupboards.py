n = int(input())

l, r = [], []

for _ in range(n):
    x, y = map(int, input().split())

    l.append(x)
    r.append(y)

l0 = l.count(0)

ans = min(l0, n - l0)
r0 = r.count(0)
ans += min(r0, n - r0)
print(ans)
