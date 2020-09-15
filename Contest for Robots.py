n = int(input())

r = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
nr, nb = 0, 0
for i in range(n):
    if r[i] > b[i]:
        nr += 1
    elif b[i] > r[i]:
        nb += 1

if not nr:
    print(-1)
else:
    if nr == 1:
        print(nb+1)
    else:
        print((nb//nr)+1)
