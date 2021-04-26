a, b = map(int, input().split())
l = []
x = 1001
m = a
n = b
f = 0
if a < b:
    m = b
    n = a
    f = 1
for i in range(m):
    if f == 0:
        l.append(i+1)
    else:
        l.append(-(i+1))
x = sum(l)
l2 = []
for i in range(n):
    l2.append(-l[i])
xx = sum(l[i:])
l2[-1] = -xx
ans = l + l2
print(*ans)
