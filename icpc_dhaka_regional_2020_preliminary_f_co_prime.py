def primeS(n):
    prime = [True for i in range(n + 1)]
    mark = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            mark.append(p)
    return mark


for t in range(1, int(input())+1):
    a, b, m = map(int, input().split())
    count, ncount = 0, 0
    dif = abs(a-b)
    isp = False

    if dif == 0:
        ncount = m
    elif dif == 1:
        ncount = 0
    else:
        prime = primeS(b+m)
        for i in prime:
            if i == dif:
                isp = True
            if i > dif:
                break
            if dif % i == 0:
                count += 1
                fir = (m+b)//i
                bi = (b-1) // i
                ncount += (fir - bi)
        if not isp and count > 1:
            fir = (m+b)//dif
            bi = (b-1) // dif
            ncount -= (fir - bi)
    print("Case {}: {}".format(t, (m+1) - ncount))
