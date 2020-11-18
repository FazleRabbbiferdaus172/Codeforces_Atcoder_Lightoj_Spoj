for _ in range(int(input())):
    l, r = map(int, input().split())
    x = r
    g = 0
    if (r-l+1) % 2 == 1:
        x = r - 1
        g = r
    if l % 2 == 0:
        mul = (-1*(x-l+1))//2
    else:
        mul = (1*(x-l+1))//2

    if r % 2 == 1:
        mul -= g
    else:
        mul += g

    print(mul)
