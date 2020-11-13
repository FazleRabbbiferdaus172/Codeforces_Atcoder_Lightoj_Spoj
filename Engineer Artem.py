for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    l = []

    for i in range(n):
        l.append([int(x) for x in input().split()])

    # print(l)

    for i in range(n):
        for j in range(m):
            if (i+j) % 2 != l[i][j] % 2:
                l[i][j] += 1

    for i in l:
        print(*i)
