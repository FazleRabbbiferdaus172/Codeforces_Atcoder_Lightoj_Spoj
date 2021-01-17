n = int(input())
a = list(map(int, input().split()))
d = dict()

for i in range(n):
    x = a[i]
    if a[i] in d:
        if d[x][1] and i - d[x][0] != d[x][1]:
            d[x] = [i, -1]
        else:
            d[x] = [i, i - d[x][0]]
    else:
        d[x] = [i, 0]
print(len([i for i in d if d[i][1] >= 0]))
for i in sorted(d.keys()):
    if d[i][1] >= 0:
        print(i, d[i][1])
