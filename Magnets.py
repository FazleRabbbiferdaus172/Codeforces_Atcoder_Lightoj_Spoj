n = int(input())
l = []
for i in range(n):
    a, b = list(input())
    l.append(a)
    l.append(b)

c = 1

for i in range(1, len(l)-1, 2):
    if l[i] == l[i+1]:
        c += 1

print(c)
