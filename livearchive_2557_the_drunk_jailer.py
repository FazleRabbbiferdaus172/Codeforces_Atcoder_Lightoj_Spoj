for _ in range(int(input())):
    n = int(input())
    l = [True]*n
    l = ["dummy"] + l

    for i in range(1, n+1):
        for j in range(i, n+1, i):
            l[j] = not l[j]
        # print(l)
    print(l.count(False))
