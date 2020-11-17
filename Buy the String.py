for _ in range(int(input())):
    n, c0, c1, h = [int(x) for x in input().split()]
    s = input()

    b1 = s.count('1')

    b0 = s.count('0')

    if c0 <= c1:
        ans = min(c0*b0+c1*b1, b1*h+n*c0)
    else:
        ans = min(c0*b0+c1*b1, b0*h+n*c1)

    print(ans)
