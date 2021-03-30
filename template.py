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


def totien_fun(n):
    ans = n
    prime = prime(n)
    '''
    let, n = (p^a) * (q^b) * (r^c)  where n is a composite number and p,q,r are prime numbers
    phi(n) = n* (p-1)/p * (q-1)/q * (r - 1)/r
           = (n/(p*q*r))(p-1)(q-1)(r-1)
    comlexity : O(sqrt(n))
    '''
    for p in prime:
        if p*p > n:
            break

        if n % p == 0:
            ans /= p
            ans *= p-1
            while n % p == 0:
                n /= p
    '''
    if n > 1 that means there is a prime number remaining that is why devide ans by n and multiply with (n-1)
    '''
    if n > 1:
        ans /= n
        ans *= n - 1

    return n


def totien_fun_till_n(n):
    '''
    value of phi of all numbers from 1 to n
    comlexity : O(n*ln(n))
    '''
    phi = [0] * (n+1)
    for i in range(1, n+1):
        phi += [i]

    prime = prime(n)

    for p in prime:
        for j in range(p, n+1, p):
            phi[j] /= p
            phi[j] *= (p-1)

    return phi
