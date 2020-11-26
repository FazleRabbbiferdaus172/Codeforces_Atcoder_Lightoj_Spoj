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


n, m, k = map(int, input().split())

st = list_input()
sc = list_input()

cho = list_input()
d = dict()
for i in range(n):
    if sc[i] in d:
        d[sc[i]].append(st[i])
    else:
        d[sc[i]] = [st[i]]

# print(d)

ans = 0

for i in range(k):
    tst = st[cho[i] - 1]
    tsc = sc[cho[i] - 1]
    l = d[tsc]
    if tst != max(l):
        ans += 1

print(ans)
