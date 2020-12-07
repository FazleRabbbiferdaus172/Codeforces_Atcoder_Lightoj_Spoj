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


n, k = map(int, input().split())
l = list_input()
l.sort()

xx = set(list(str(n)))
# print(xx)
nai = True

for i in xx:
    if int(i) in l:
        nai = False
        break

if nai:
    print(n)
else:

    while not nai:
        n += 1
        nai = True
        xx = set(list(str(n)))

        for i in xx:
            if int(i) in l:
                nai = False
                break
    print(n)
