
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]

    #row = [[] for x in range(n)]
    #col = [[] for x in range(m)]
    row, col = [], []
    for i in range(n):
        l = [int(x) for x in input().split()]
        row.append(l)

    for i in range(m):
        l = [int(x) for x in input().split()]
        col.append(l)

    for i in col[0]:
        for j in row:
            if i in j:
                print(*j)
