n = int(input())

h, a = [], []

for i in range(n):
    w, e = [x for x in input().split(' ')]
    h.append(w)
    a.append(e)
m = 0
for i in h:
    if i in a:
        m += a.count(i)

print(m)
