for _ in range(int(input())):
    p, a, b, c = map(int, input().split())

    x, y, z = (a - p % a) % a, (b - p % b) % b, (c - p % c) % c
    print(min(x, y, z))
