import sys
import math
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


def lcm(*n):
    ans = 1
    for i in n:
        ans *= (i//gcd(i, ans))
    return ans


def gcd(*n):
    ans = 0
    for i in n:
        ans = math.gcd(ans, i)
    return ans


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


da = [[-1]*100 for i in range(100+1)]


def ncr(n, m):
    '''
    **Here m means r**
    ****Do not foget to intial 'da' everytime if there are multiple test cases*****
    based on formula: n C r + n C (r-1) = (n+1) C r then (n - 1) C r + (n - 1) C (r - 1) = n C r
    '''
    global da
    if m == 1:
        ans = n
    elif n == m or m == 0:
        ans = 1
    elif da[n-1][m] != -1 and da[n-1][m-1] != -1:
        ans = da[n-1][m] + da[n-1][m-1]
    else:
        ans = ncr(n-1, m) + ncr(n-1, m-1)
        da[n][m] = ans
    return ans


def totien_fun(n):
    ans = n
    prime = prime(n)
    #prime = []
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
    #prime = []

    for p in prime:
        for j in range(p, n+1, p):
            phi[j] /= p
            phi[j] *= (p-1)

    return phi


def factorial_till_n(n, MOD):
    '''
    complexity: O(n)
    '''
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = (i * fact[i-1]) % MOD

    return fact


def inverse_factorial_till_n(n, MOD):
    '''
    Params: n, MOD
    complexity: O(n)
    '''
    fact = factorial_till_n(n, MOD)
    i_fact = [1]*(n+1)
    i_fact[n] = binpow(fact[n], MOD - 2)

    for i in range(n-1, -1, -1):
        i_fact[i] = ((i+1)*i_fact[i+1]) % MOD

    return i_fact


def ncr_liner(n, r, MOD):
    '''
    ***BETTER if you copy and paste in the main finction. if you call it everytime the time complecity won't be O(n)***
    complexity: O(n)
    '''
    fact = factorial_till_n(n, MOD)
    i_fact = inverse_factorial_till_n(n, MOD)
    ncr = (fact[n] * (i_fact[r])) % MOD
    ncr = ncr * (i_fact[n-r]) % MOD
    return ncr


# print("{:.6f}".format(ans))


print(ncr_liner(10, 5, 127))
