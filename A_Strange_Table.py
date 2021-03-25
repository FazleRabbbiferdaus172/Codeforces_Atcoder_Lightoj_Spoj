for _ in range(int(input())):
    n, m, x = map(int, input().split())

    yc = x // n

    if x % n > 0:
        yc += 1
    xc = x - (yc-1)*n
    #print("cord", xc, yc)
    ans = (xc-1)*m + yc
    print(ans)
