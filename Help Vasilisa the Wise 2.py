r1, r2 = [int(x) for x in input().split()]
c1, c2 = [int(x) for x in input().split()]
d1, d2 = [int(x) for x in input().split()]

x2 = (c2 + r1 - d1)//2

x1 = r1 - x2

y1 = d2 - x2

y2 = c2 - x2

if 1 <= x1 <= 9 and 1 <= x2 <= 9 and 1 <= y1 <= 9 and 1 <= y2 <= 9 and x1 != x2 and y1 != y2 and x1 != y1 and x1 != y2 and x2 != y1 and x2 != y2 and x1+x2 == r1 and y1+y2 == r2 and x1+y1 == c1 and x2+y2 == c2 and x1+y2 == d1 and y1+x2 == d2:
    print(x1, x2)
    print(y1, y2)
else:
    print(-1)
