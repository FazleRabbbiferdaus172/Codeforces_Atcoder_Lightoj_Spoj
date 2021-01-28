n, k = map(int, input().split())
s = list(input())

ss = set(s)
l = []
for i in ss:
    l.append(s.count(i))
ans = 0
while k:
    i = l.index(max(l))
    t = min(k, l[i])
    ans += t*t
    l[i] = -1
    k -= t
print(ans)
