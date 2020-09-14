for _ in range(int(input())):
    n, d = [int(x) for x in input().split()]

    p = [int(x) for x in input().split()]

    np = p[0]
    for i in range(1, n):
        if i*p[i] > d:
            np += d//i
            break
        np += p[i]
        d -= i*p[i]
    print(np)
