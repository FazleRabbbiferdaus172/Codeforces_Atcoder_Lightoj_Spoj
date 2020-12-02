chk = [[0]*3 for _ in range(3)]

l = []

for _ in range(3):
    j = [int(x) for x in input().split()]
    l.append(j)


for i in range(3):
    for j in range(3):
        xx = l[i][j]
        for x in range(max(0, j-1), min(j+1+1, 3)):
            chk[i][x] += xx
        for x in range(max(0, i-1), min(i+1+1, 3)):
            if x == i:
                continue
            chk[x][j] += xx
# print(chk)
for i in chk:
    xx = [str((x+1) % 2) for x in i]
    print("".join(xx))
