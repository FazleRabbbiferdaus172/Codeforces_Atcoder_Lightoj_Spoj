for _ in range(int(input())):
    a, b = map(int, input().split())
    x, y = min(a, b), max(a, b)

    print((x+x)*(x+x) if x+x >= y else y*y)
