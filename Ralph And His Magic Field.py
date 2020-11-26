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
    MOD = int(1e9) + 7
    while n:
        if n & 1:
            #ans *= a
            ans = (ans * a) % MOD
        #a *= a
        a = (a*a) % MOD
        n >>= 1
    return ans


n, m, k = map(int, input().split())

if not n % 2 == m % 2 and k == -1:
    print(0)
else:
    print(binpow(2, (n-1)*(m-1)))
