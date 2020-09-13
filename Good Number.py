n, k = [int(x) for x in input().split()]
c = 0
for i in range(n):
    l = [int(x) for x in list(str(input()))]
    d = dict()
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    j = list(d.keys())
    nt = True
    for i in range(k+1):
        if not i in j:
            nt = False
    if nt:
        c += 1

print(c)
