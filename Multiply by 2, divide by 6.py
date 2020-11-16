for _ in range(int(input())):
    n = int(input())

    c2, c3 = 0, 0

    while n % 2 == 0:
        c2 += 1
        n //= 2

    while n % 3 == 0:
        c3 += 1
        n //= 3

    if c2 > c3 or n > 1:
        print(-1)
    else:
        print(c3 + (c3 - c2))
