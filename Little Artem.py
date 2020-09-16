for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    r = []
    for i in range(n):
        s = "B"*m
        r.append(s)

    s = list(r[-1])
    s[-1] = 'W'
    s = "".join(s)
    r[-1] = s
    for i in r:
        print(i)
