n = int(input())
l = [int(x) for x in input().split()]
flag = False
chk = []
for i in l:
    if i % 2 == 1:
        chk.append(1)
    else:
        chk.append(0)

if chk.count(1) == n or chk.count(1) == 0:
    print(*l)
else:
    print(*sorted(l))
