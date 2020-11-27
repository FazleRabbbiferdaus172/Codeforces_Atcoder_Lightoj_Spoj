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
allrem = [0] * k
for i in l:
    allrem[i % k] += 1
ans = allrem[0] - (allrem[0] % 2)
# print(allrem)
for i in range(1, k):
    #print(i, k-i)
    if i == k - i:
        ans += allrem[i] - (allrem[i] % 2)
    else:
        ans += min(allrem[i], allrem[k-i])
print(ans)
