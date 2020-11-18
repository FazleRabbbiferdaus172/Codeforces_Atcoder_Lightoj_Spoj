for _ in range(int(input())):
    n, q = map(int, input().split())

    m = []

    for i in range(1, 11):
        m.append((q*i) % 10)

    ans = sum(m)
    jj = (n % (q*10))//q
    #print(ans, jj)
    ans = (n//(q*10))*ans + sum(m[:jj])
    print(ans)
