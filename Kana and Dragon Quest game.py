for _ in range(int(input())):

    h, n, m = map(int, input().split())
    f = False
    while n:
        if h <= m*10:
            print("YES")
            f = True
            break
        h = h//2 + 10
        n -= 1
    if h <= m*10 and not f:
        print("YES")
        f = True
    if not f:
        print("NO")
