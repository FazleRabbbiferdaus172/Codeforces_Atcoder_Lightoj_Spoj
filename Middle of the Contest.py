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


h1, m1 = [int(x) for x in input().split(':')]
h2, m2 = [int(x) for x in input().split(':')]

start = h1*60 + m1
end = h2*60 + m2

add = (end - start)//2
addm, addh = add % 60, add // 60

ansh, ansm = h1+addh+(m1+addm)//60, (m1+addm) % 60
if ansh < 10:
    ansh = "0" + str(ansh)
else:
    ansh = str(ansh)
if ansm < 10:
    ansm = "0" + str(ansm)
else:
    ansm = str(ansm)
print("{}:{}".format(ansh, ansm))
