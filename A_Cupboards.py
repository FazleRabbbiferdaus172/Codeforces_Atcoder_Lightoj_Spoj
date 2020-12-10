n = int(input())

l, r = [], []

for _ in range(n):
    x, y = map(int, input().split())

    l.append(x)
    r.append(y)

l0, l1 = l.count(0), l.count(1)

ans = min(l0, l1)
r0, r1 = r.count(0), r.count(1)
ans += min(r0, r1)
print(ans)
