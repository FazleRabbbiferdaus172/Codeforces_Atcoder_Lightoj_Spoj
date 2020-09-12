n = int(input())
l = []
for _ in range(n):
    l.append(list(input()))

s = set()
i, j = 0, n-1
dig = True
p = l[0][0]
for x in l:
    if x[i] != x[j] or x[i] != p:
        dig = False
        break
    if x.count(p) != 2 and i != j:
        dig = False
        break
    elif x.count(p) != 1 and i == j:
        dig = False
        break
    i += 1
    j -= 1
    for y in x:
        s.add(y)
    if len(s) != 2:
        dig = False
        break

if dig and len(s) == 2:
    print("YES")

else:
    print("NO")
