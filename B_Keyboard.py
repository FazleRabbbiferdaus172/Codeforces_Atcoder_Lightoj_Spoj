n, m, x = map(int, input().split())
g = []
keyB = {}
isS = []
d = {}
for i in range(n):
    z = list(input())
    g.append(z)

q = input()
s = input()
for i in range(n):
    for j in range(m):
        if g[i][j] != 'S':
            keyB[g[i][j]] = (i, j)
        else:
            isS += [(i, j)]
isS.sort()
# print(isS)
count = 0
for i in s:
    if not i.lower() in keyB:
        print(-1)
        break
    if i.isupper() and len(isS) == 0:
        print(-1)
        break
    if i.isupper() and len(isS) > 0:
        #print("FOR: ", i)
        for j in isS:
            dist = ((keyB[i.lower()][0]-j[0])**2 +
                    (keyB[i.lower()][1]-j[1])**2)**.5
            #print(keyB[i.lower()], j, dist)
            if dist <= x:
                # print("YES")
                break
        else:
            count += 1
        #print("END: ", i)
        # print()
else:
    print(count)
