

for _ in range(int(input())):
    p, q = [int(x) for x in input().split()]
    c = q
    d = p

    i = 1
    factor = []
    while i*i <= q:
        if q % i == 0:
            factor.append(i)
            if q//i != i:
                factor.append(q//i)
        i += 1

    # print(factor)
    factor.remove(1)
    m = 1
    for i in factor:
        d = p
        while d % c == 0:
            d //= i
        m = max(m, d)
        #print(m, d)

    print(m)
