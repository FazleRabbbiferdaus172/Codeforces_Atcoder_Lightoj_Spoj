def binpow(a, n, MOD):
    ans = 1
    while n:
        if n & 1:
            #ans *= a
            ans = (ans * a) % MOD
        #a *= a
        a = (a*a) % MOD
        n >>= 1
    return ans


while True:
    try:

        a = int(input())
        n = int(input())
        MOD = int(input())

        print(binpow(a, n, MOD))
        input()
    except(EOFError):
        break
