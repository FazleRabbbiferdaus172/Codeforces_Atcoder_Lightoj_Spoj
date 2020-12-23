for _ in range(int(input())):
    n = int(input())
    ans = (n*(n+1))//2

    i = 0
    while 2**i <= n:
        ans -= (2**i)*2
        i += 1

    print(ans)
