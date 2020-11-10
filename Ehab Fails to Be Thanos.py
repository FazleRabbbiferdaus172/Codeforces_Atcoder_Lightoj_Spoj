n = int(input())
l = [int(x) for x in input().split()]
c = l.count(l[0])
if c == 2*n:
    print(-1)
else:
    print(*sorted(l))
