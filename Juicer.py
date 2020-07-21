n, m, d = [int(x) for x in input().split()]
l = [int(x) for x in input().split() if int(x) <= m]
c = 0
s = 0
for i in l:
    s += i
    if s > d:
        c += 1
        s = 0

print(c)
