def pwm(a, n, mod):
    ans = 1
    while n:
        if n & 1:
            ans = ans*a % mod

        a = a*a % mod
        n >>= 1
    return ans


n = int(input())

l = [int(x) for x in input().split()]

l.sort()

a, b = l[:n], l[n:]
ans = 0
mod = 998244353
dnom = 1
nom = 1
for i in range(n):
    ans += (b[i] % mod - a[i] % mod) % mod
    nom = nom * (i+1) % mod * (2*n - i) % mod
    dnom = dnom*(i+1) % mod * (i+1) % mod
gg = (nom % mod)*pwm(dnom, mod-2, mod) % mod
fans = (ans*gg) % mod

# print(ans)
# print(gg)
print(fans)
