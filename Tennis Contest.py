from math import *


def ncr(n, r):
    p = 1
    k = 1
    if (n - r < r):
        r = n - r
    if (r != 0):
        while (r):
            p *= n
            k *= r
            m = gcd(p, k)
            p //= m
            k //= m
            n -= 1
            r -= 1
    else:
        p = 1
    return p


def binpow(a, n):
    ans = 1
    while n:
        if n & 1:
            ans *= a
        a *= a
        n >>= 1
    return ans


for _ in range(int(input())):
    n = int(input())
    p = float(input())
    ans = 0
    for i in range(n, 2*n):
        ans += ncr(2*n-1, i)*binpow(p, i)*binpow(1-p, 2*n-1-i)
    ans = round(ans, 2)
    print("{0:.2f}".format(ans))
