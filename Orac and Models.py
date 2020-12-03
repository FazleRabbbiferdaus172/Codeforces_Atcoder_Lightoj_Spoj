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


for _ in range(int(input())):
    n = int(input().strip())
    l = list_input()
    l.insert(0, -1)
    ans = [1]*int(1e6)

    for i in range(1, n+1):
        for j in range(i*2, n+1, i):
            #print(l[i], j, l[j])
            if l[i] < l[j]:
                ans[j] = max(ans[j], ans[i]+1)
                # print(ans[1:n+1])
    anss = 0
    for i in range(1, n+1):
        anss = max(anss, ans[i])
    print(anss)
