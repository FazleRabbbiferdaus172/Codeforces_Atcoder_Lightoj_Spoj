for i in range(int(input())):
    n, x = map(int, input().split())

    l = list(map(int, input().split()))
    ans = 0
    where = [0]*n

    for i in range(n):
        xx = l[i]
        while xx % x == 0:
            xx //= x
            where[i] += 1

    doit = min(where)
    doit_ind = where.index(doit)
    # print(where)
    #print(doit, doit_ind)
    for i in l:
        ans += (doit+1)*i

    for i in range(doit_ind):
        ans += l[i]

    print(ans)
