for _ in range(int(input())):
    a, b, c, d = [int(z) for z in input().split()]

    print(max(a+b, c+d))
