n = int(input())

l = [int(x) for x in input().split()]
nuc, p = 0, 0
for i in l:
    if i > 0:
        p += i
    else:
        if p == 0:
            nuc -= i
        elif p > 0:
            p += i


print(nuc)
