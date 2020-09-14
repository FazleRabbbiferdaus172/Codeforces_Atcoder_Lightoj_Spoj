t = int(input())

for _ in range(t):
    x, y, a, b = [int(x) for x in input().split()]

    if (y-x) % (a+b) == 0:
        print((y-x) // (a+b))
    else:
        print(-1)
