for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]

    a, b = [int(x) for x in input().split()]

    if (not a and not b) or not a:
        print(0)
    else:
        one_n = max(x, y)-min(x, y)

        if b < 2*a:
            b = b
        else:
            b = a*2

        if one_n == 0:
            print(x*b)
        else:
            print(one_n*a+(max(x, y)-one_n)*b)
