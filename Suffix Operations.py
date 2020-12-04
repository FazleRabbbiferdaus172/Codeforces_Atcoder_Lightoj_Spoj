import sys
input = sys.stdin.readline


def list_input():
    return list(map(int, input().split()))


def float_compare(a, b):
    if abs(a-b) < float(1e-9):
        return True
    else:
        return False


def sub_mod(x, mod):
    x = x % mod
    if x < 0:
        x += mod
    return x


def divisor(n):
    i = 1
    dv = []
    while i*i <= n:
        if n % i == 0:
            dv.append(i)
            if i*i != n:
                dv.append(n//i)
        i += 1

    return dv


def binpow(a, n):
    ans = 1
    # MOD =
    while n:
        if n & 1:
            ans *= a
            #ans =  (ans * a) % MOD
        a *= a
        #a = (a*a) % MOD
        n >>= 1
    return ans


for _ in range(int(input().strip())):
    n = int(input().strip())
    l = list_input()
    cou = 0
    if n == 1:
        print(0)
    else:
        for i in range(1, n):
            cou += abs(l[i] - l[i-1])
        m = -1
        for i in range(1, n-1):
            xx = abs(l[i] - l[i-1]) + abs(l[i+1] - l[i]) - abs(l[i+1] - l[i-1])
            m = max(xx, m)
        m = max(abs(l[0] - l[1]), abs(l[-1] - l[-2]), m)
        print(cou - m)
