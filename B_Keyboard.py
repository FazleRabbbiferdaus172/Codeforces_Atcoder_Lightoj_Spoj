n, m, x = map(int, input().split())
g = []
keyB = {}
isS = []
d = {}
for i in range(n):
    z = list(input())
    g.append(z)
    if 'S' in z:
        isS += [(i, z.index('S'))]
isS.sort()
q = input()
s = input()

for i in range(n):
    for j in range(m):
        if g[i] != 'S':
            keyB[g[i][j]] = (i, j)
count = 0
for i in s:
    if not i.lower() in keyB:
        print(-1, 1)
        break
    if i.isupper() and len(isS) == 0:
        print(-1, 1)
        break
    if i.isupper() and len(isS) > 0:
        for j in isS:
            dist = ((keyB[i.lower()][0]-j[0])**2 -
                    (keyB[i.lower()][1]-j[1])**2)**.5
            if dist <= x:
                break
        else:
            count += 1


print(count)
