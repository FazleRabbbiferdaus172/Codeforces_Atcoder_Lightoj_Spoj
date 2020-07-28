n = int(input())
l = [int(x) for x in input().split()]
s = l
a, b, c = 0, 0, 0
if 1 in l and 2 in l and 3 in l:
    k = min(l.count(1), l.count(2), l.count(3))
    print(k)
    for i in range(k):
        a, b, c = l.index(1, a), l.index(2, b), l.index(3, c)
        a += 1
        b += 1
        c += 1
        print(a, b, c)
else:
    print(0)
