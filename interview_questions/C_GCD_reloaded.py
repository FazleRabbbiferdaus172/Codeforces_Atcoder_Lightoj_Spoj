for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(0, 0)
    else:
        ex = abs(a-b)
        m = min(a % ex, ex - a % ex)
        print(ex, m)
