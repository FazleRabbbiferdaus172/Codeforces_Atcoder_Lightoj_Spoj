for _ in range(int(input())):
    x, y, a, b = [int(x) for x in input().split()]
    r1 = b*a
    r2 = (x-a-1)*y
    r3 = (y-b-1)*x
    r4 = x*b
    r5 = y*a
    #print(r1, r2, r3, r4, r5)
    print(max(r1, r2, r3, r4, r5))
