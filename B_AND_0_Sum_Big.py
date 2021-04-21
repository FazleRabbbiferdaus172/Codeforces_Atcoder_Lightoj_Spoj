for _ in range(int(input())):
    n, k = map(int, input().split())
    mod = 1000000007
    ans = 1
    for i in range(k):
        ans *= n
        ans %= mod
    print(ans % mod)
