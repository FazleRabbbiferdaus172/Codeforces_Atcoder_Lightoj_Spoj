s, n = map(int, input().split())
remain = []
killed = 0
for _ in range(n):
    ds, b = map(int, input().split())

    if s > ds:
        s += b
        killed += 1
    else:
        remain += [(ds, b)]


remain.sort()

for i in remain:

    if s > i[0]:
        s += i[1]
        killed += 1

if killed == n:
    print("YES")
else:
    print("NO")
