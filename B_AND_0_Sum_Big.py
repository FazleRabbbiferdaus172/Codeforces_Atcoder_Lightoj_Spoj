for _ in range(int(input())):
    n, k = map(int, input().split())
    mod = 1000000007
    ans = 0
    for i in range((2**k) // 2):
        if i == 0:
            ans += n
        else:
            ans += (n * (n-1))
    print(ans % mod)
