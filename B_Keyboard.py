n, m, xx = map(int, input().split())
g = []
keyB = {}
isS = []
d = {}
for i in range(n):
    z = list(input())
    g.append(z)

q = input()
s = input()

for i in range(ord('a'), ord('z')+1):
    keyB[chr(i)] = -1
    keyB[chr(i).upper()] = -1
for i in range(n):
    for j in range(m):
        if g[i][j] == 'S':
            isS += [(i, j)]

for i in range(n):
    for j in range(m):
        ltr = g[i][j]
        if ltr.islower():
            keyB[ltr] = 0
            ltr = ltr.upper()
            if keyB[ltr] < 0 and len(isS) > 0:
                keyB[ltr] = 1
            for (x, y) in isS:
                dist = ((x-i)**2 + (y-j)**2)**.5
                #print("for {} dist is {} and given x is {}".format(ltr, dist, x))
                if dist <= xx:
                    keyB[ltr] = 0
                    break
# print(keyB)
# isS.sort()
# print(isS)
# print(keyB)
count = 0
for i in s:
    if keyB[i] == -1:
        print(-1)
        break
    else:
        count += keyB[i]
else:
    print(count)
